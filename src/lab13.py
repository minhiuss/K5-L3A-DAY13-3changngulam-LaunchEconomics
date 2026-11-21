"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def in_nhiem_vu_a(runs, reqs):
    """In kết quả Nhiệm vụ A1, A2, A3, A4 (CP1)."""
    print('--- A1 · Ba phép thử đáp án biết trước ---')
    print(f'Tối đa 2 lần (p=0.8):          {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'Chạy đến khi đúng (p=0.8):     {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'Hệ số chi phí tối đa 3 lần:    {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    kiem_tra_dap_an_biet_truoc()

    print('\n--- A2 · Mô hình chi phí từ trace (có phần simulated) ---')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:16s} {gia_tri:>12,.1f}')
        else:
            print(f'{ten:16s} {gia_tri:>12,.0f}')
    ti_le_gap = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Gấp hoá đơn/yc:  {ti_le_gap:>11.1f}x')
    print(f'Tỉ trọng xem lại:{ket_qua["xem_lai"] / ket_qua["tong"] * 100:>11.1f}% (simulated)')
    print(f'Tỉ trọng làm lại:{ket_qua["lam_lai"] / ket_qua["tong"] * 100:>11.1f}% (simulated)')
    print(f'Hệ thống/yêu cầu:{he_thong_moi_yc:>12,.0f} ({he_thong_moi_yc / BASELINE:.2f}x, simulated)')

    print('\n--- A3 · Tách theo loại yêu cầu (CPS là simulated) ---')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r_sub = runs[runs['request_id'].isin(sub['request_id'])]
        kq = mo_hinh(runs, sub)
        print(
            f'{loai:10s} | yc={len(sub):3d} | tc={kq["thanh_cong"]/len(sub)*100:5.1f}%'
            f' | chay/yc={len(r_sub)/len(sub):.2f} | cps={kq["cps"]:>7,.0f}'
            f' | so_12k={kq["cps"]/BASELINE:.2f}x'
        )
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(int)
    print('\nTỉ lệ status=ok (%) theo lần thử (attempt):')
    print((merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100).round(1))

    print('\n--- A4 · Chi phí cố định 40 triệu/tháng (noi_dia + hang_nang, simulated) ---')
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_scope = mo_hinh(runs, scope)
    ty_le_tc_mau = kq_scope['thanh_cong'] / len(reqs)
    chi_phi_co_dinh = 40_000_000
    print(f'Biến đổi trong phạm vi: {kq_scope["tong"]:,.0f} / {kq_scope["thanh_cong"]} = {kq_scope["cps"]:,.0f} đ (simulated)')
    for ten_kl, khoi_luong in [('45.000 yc/tháng', 45_000), ('Một nửa (22.500)', 22_500)]:
        viec_tc_thang = khoi_luong * ty_le_tc_mau
        co_dinh_viec = chi_phi_co_dinh / viec_tc_thang
        tong_viec = kq_scope['cps'] + co_dinh_viec
        print(
            f'{ten_kl:18s} | tc/thang={viec_tc_thang:>7,.0f}'
            f' | co_dinh={co_dinh_viec:>5,.0f} | tong={tong_viec:>5,.0f} ({tong_viec/BASELINE:.2f}x)'
        )
    hoa_von_tc = chi_phi_co_dinh / (BASELINE - kq_scope['cps'])
    hoa_von_yc = hoa_von_tc / ty_le_tc_mau
    print(f'Ngưỡng hoà vốn 12k: >= {hoa_von_tc:,.0f} việc thành công/tháng (>= {hoa_von_yc:,.0f} yc/tháng)')


def tinh_nhiem_vu_b(runs, reqs):
    """Tính các kịch bản độ nhạy B1-B4 từ cùng mô hình chi phí của CP1."""
    goc = mo_hinh(runs, reqs)
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    b1 = {}
    for ten, tham_so in kich_ban.items():
        ket_qua = mo_hinh(runs, reqs, **tham_so)
        b1[ten] = {
            'cps': ket_qua['cps'],
            'thay_doi_pct': (ket_qua['cps'] / goc['cps'] - 1) * 100,
        }

    b2 = mo_hinh(
        runs,
        reqs,
        gia_vao=52,
        gia_ra=260,
        he_so_xem_lai=2,
    )
    b2['thay_doi_pct'] = (b2['cps'] / goc['cps'] - 1) * 100

    b3 = {}
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        b3[gioi_han] = {
            **ket_qua,
            'khong_thanh_cong': khong_thanh_cong,
            'chi_phi_he_thong': ket_qua['tong'] + khong_thanh_cong * BASELINE,
        }

    # B4 chỉ xét hai loại nằm trong phạm vi pilot. Một yêu cầu có ít nhất
    # một lần status=ok sẽ được nhân viên xem lại đúng một lần.
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    scope_runs = runs[runs['request_id'].isin(scope['request_id'])]
    chi_phi_may = mo_hinh(runs, scope)
    so_xem_lai = scope_runs.loc[scope_runs['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = (scope['ket_qua'] == 'lam_lai').sum()
    thanh_cong = (scope['ket_qua'] == 'thanh_cong').sum()
    token_tool = chi_phi_may['token'] + chi_phi_may['tool']

    def b4_voi_phut_lam_lai(phut_lam_lai):
        xem_lai = so_xem_lai * 5 * LUONG_PHUT
        lam_lai = so_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = token_tool + xem_lai + lam_lai
        return {
            'phut_lam_lai': phut_lam_lai,
            'xem_lai': xem_lai,
            'lam_lai': lam_lai,
            'tong': tong,
            'cps': tong / thanh_cong,
            'so_voi_baseline': tong / thanh_cong / BASELINE,
            'phut_xem_lai_hoa_von': (
                BASELINE * thanh_cong - token_tool - lam_lai
            ) / (so_xem_lai * LUONG_PHUT),
        }

    phut_lam_lai_do_tu_mau = round(
        reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean(),
        1,
    )
    b4 = {
        'so_yeu_cau': len(scope),
        'so_xem_lai': so_xem_lai,
        'so_lam_lai': so_lam_lai,
        'thanh_cong': thanh_cong,
        'token_tool': token_tool,
        'de_bai_9_phut': b4_voi_phut_lam_lai(9),
        'do_tu_mau': b4_voi_phut_lam_lai(phut_lam_lai_do_tu_mau),
    }
    return {'goc': goc, 'b1': b1, 'b2': b2, 'b3': b3, 'b4': b4}


def in_nhiem_vu_b(runs, reqs):
    """In bảng độ nhạy và các phép tính B1-B4 (CP2)."""
    ket_qua = tinh_nhiem_vu_b(runs, reqs)

    print('\n--- B1 · Đổi từng yếu tố (simulated) ---')
    print(f'{"Kịch bản":30s} {"CPS":>10s} {"Thay đổi":>10s}')
    for ten, dong in ket_qua['b1'].items():
        print(f'{ten:30s} {dong["cps"]:>9,.0f}đ {dong["thay_doi_pct"]:>+9.1f}%')

    b2 = ket_qua['b2']
    print('\n--- B2 · Đổi một cặp (simulated) ---')
    print(f'Token ×2 và xem lại ×2: {b2["cps"]:,.0f}đ ({b2["thay_doi_pct"]:+.1f}%)')
    print('Xếp hạng: 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên')

    print('\n--- B3 · Giới hạn chạy lại (simulated) ---')
    print(f'{"Giới hạn":10s} {"Trợ lý":>12s} {"Không TC":>10s} {"Hệ thống":>12s} {"CPS":>10s}')
    for gioi_han, dong in ket_qua['b3'].items():
        print(
            f'{gioi_han:>2d} lần     {dong["tong"]:>11,.0f}đ'
            f' {dong["khong_thanh_cong"]:>10,d} {dong["chi_phi_he_thong"]:>11,.0f}đ'
            f' {dong["cps"]:>9,.0f}đ'
        )

    b4 = ket_qua['b4']
    print('\n--- B4 · Xem lại 100%, noi_dia + hang_nang (simulated) ---')
    print(
        f'{b4["so_yeu_cau"]} yêu cầu, {b4["so_xem_lai"]} ca xem lại, '
        f'{b4["so_lam_lai"]} ca làm lại, {b4["thanh_cong"]} việc thành công'
    )
    for ten, khoa in [('Đề bài 9 phút', 'de_bai_9_phut'), ('Mẫu 15,3 phút', 'do_tu_mau')]:
        dong = b4[khoa]
        print(
            f'{ten:17s}: tổng={dong["tong"]:>11,.0f}đ, cps={dong["cps"]:>8,.0f}đ '
            f'({dong["so_voi_baseline"]:.2f}x), hoà vốn xem lại ≤ {dong["phut_xem_lai_hoa_von"]:.1f} phút'
        )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
