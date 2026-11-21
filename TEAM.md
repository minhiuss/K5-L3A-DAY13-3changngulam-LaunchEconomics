# Team

## Thông tin nhóm

- Tên nhóm: 3changngulam
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-3changngulam-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: [https://github.com/minhiuss/K5-L3A-DAY13-3changngulam-LaunchEconomics](https://github.com/minhiuss/K5-L3A-DAY13-3changngulam-LaunchEconomics) · nhánh nộp: `main` · commit chốt nội dung: `d1b2e6f` (commit cuối trên `main` chỉ cập nhật dòng này và thành viên)

## Thành viên


| STT | Họ tên           | MSSV        | Email                                                         | GitHub      | Vai trò                          |
| ---: | ---------------- | ----------- | ------------------------------------------------------------- | ----------- | -------------------------------- |
| 1   | Nguyễn Văn Nhi   | 2A202603697 | [nguyenvannhi224@gmail.com](mailto:nguyenvannhi224@gmail.com) | hagasei     | Người viết code (phụ trách CP1, tổng hợp CP5) |
| 2   | Ngô Huy Hoàng    | 2A202603622 | —                                                             | HuyHoangg10 | Người kiểm số (phụ trách CP2, phiếu chấm hội đồng Gate 2a) |
| 3   | Nguyễn Ngọc Toàn | 2A202603405 | ngoctoan140604@gmail.com                                      | jpack1      | Người gắn nhãn 1 (Phụ trách CP3) |
| 4   | Đỗ Minh Hiếu     | 2A202603402 | mhieudo11102@gmail.com                                        | minhius     | Người gắn nhãn 2 kiêm giữ hồ sơ (Phụ trách CP4 + repo nhóm) |
| 5   | Nguyễn Đức Trung | 2A202603423 | trungducnguyen2k@gmail.com                                    | NguyenDucTrung999 | Phụ trách CP5 (chỉ số, event, rủi ro kinh tế) |


Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenVanNhi-2A202603697

### Phần việc phụ trách

- Người viết code — phụ trách CP1 (Nhiệm vụ A: Mô hình chi phí mỗi việc thành công) và tổng hợp CP5 (Nhiệm vụ E: chỉ số, rủi ro kinh tế, hồ sơ launch v0, báo cáo nhóm).

### Đóng góp cụ thể

- Hiện thực 3 hàm kinh tế chạy lại ở A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), vượt qua 3 phép thử đáp án biết trước (`1,20` · `1,25` · `1,25`).
- Hiện thực hàm `mo_hinh(runs, reqs, ...)` ở A2 và hàm `in_nhiem_vu_a(runs, reqs)` tính chi phí từ trace (A2), tách theo 4 loại yêu cầu kèm tỉ lệ `status=ok` theo từng lần thử (A3), và tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4).
- Điền hoàn chỉnh kết quả và câu trả lời các mục A1, A2, A3, A4 (kèm nhãn `simulated` đầy đủ) vào `report/team/bang_chi_phi.md`.
- Tổng hợp CP5: tính chỉ số chính E1 trong `src/lab13.py` (`82,83%` toàn mẫu, `92,26%` trong phạm vi), hoàn thiện `report/team/chi_so.md` (5 chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế), `report/team/ho_so_launch_v0.md` (7 mục và đề xuất `Go có điều kiện`) và `report/team/group_report.md`.

### Bằng chứng

- Code: `src/lab13.py` (các hàm A1, `mo_hinh`, `in_nhiem_vu_a`, phần in chỉ số E1).
- Hồ sơ: `report/team/bang_chi_phi.md` (A1–A4), `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`.
- Báo cáo cá nhân: `report/team/2A202603697_NguyenVanNhi.md`.

## NgoHuyHoang-2A202603622

### Phần việc phụ trách

- Người kiểm số — phụ trách CP2 (Nhiệm vụ B: bảng độ nhạy) và chấm duyệt chéo Gate 2a (`phieu_cham.md`).

### Đóng góp cụ thể

- Viết phần tính B1–B4 trong `src/lab13.py`, dùng lại hàm `mo_hinh()` của CP1 thay vì điền số cố định.
- Hoàn thiện 9 kịch bản B1, kịch bản kết hợp B2, so sánh giới hạn chạy lại B3 và trường hợp xem lại 100% ở B4.
- Điền kết quả CP2 vào `report/team/bang_chi_phi.md` và gắn nhãn `simulated` cho các số liên quan.
- Chấm chéo hồ sơ nhóm `XinCaiTen` (26/30 điểm, quyết định `Go có điều kiện`) vào `report/team/phieu_cham.md`.

### Bằng chứng

- Code: `src/lab13.py` (`tinh_nhiem_vu_b`, `in_nhiem_vu_b`).
- Hồ sơ: `report/team/bang_chi_phi.md` (B1–B4), `report/team/phieu_cham.md` (commit `0c3b9b4`).
- Báo cáo cá nhân: `report/team/2A202603622_NgoHuyHoang.md`.

## Nguyễn Ngọc Toàn (2A202603405)

### Phần việc phụ trách

- Người gắn nhãn 1, phụ trách theo dõi yêu cầu CP3 và tổng hợp bảng phân loại lỗi, cách khắc phục cho trợ lý hoàn phí.

### Đóng góp cụ thể

- Chuẩn bị bảng tham khảo cho 20 ca lỗi với hỗ trợ của AI và đối chiếu nhãn với slide chữa.
- Hoàn thiện bảng khắc phục cho 5 loại lỗi, mỗi ca có sự kiện phát hiện, ngưỡng cảnh báo, tần suất kiểm tra và vai trò phụ trách.

### Bằng chứng

- [Bảng lỗi và cách khắc phục CP3](report/team/bang_loi.md).
- Báo cáo cá nhân: [report/team/2A202603405_NguyenNgocToan.md](report/team/2A202603405_NguyenNgocToan.md) (commit `d137446`).

## DoMinhHieu-2A202603402

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ — phụ trách CP4 (Nhiệm vụ D: `pilot_plan.yaml`) và tạo, quản lý repo nhóm (fork, đồng bộ với repo đề, đổi tên theo mẫu).

### Đóng góp cụ thể

- Viết hàm `co_mau(p1, p2)` và khối `TODO CP4` trong `src/lab13.py`: tính năm câu D1 (`1.251` · DE `2,48` → 42 người/nhóm, không đủ người · tối đa `1.000` · tối đa `300` · m ≥ `299`, DE `6,96`) và power `0,64` nếu tác động thật chỉ 5 điểm.
- Trả lời năm câu D2 cho cách chia theo nhân viên 20 + 20, ghi đánh đổi đã chấp nhận (mde 6 điểm).
- Tính số nền trước khi đặt luật dừng (mở lại `3,97%`, bỏ qua gợi ý `21,09%` trong phạm vi) và điền đủ `report/team/pilot_plan.yaml` với ba luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- Xử lý conflict khi ghép code CP4 với CP1/CP2 để `python lab13.py` chạy hết.

### Bằng chứng

- Commit `edce320` (D1) và `671f570` (power, D2, D3).
- Code: `src/lab13.py` (`co_mau`, khối `TODO CP4`).
- Hồ sơ: `report/team/pilot_plan.yaml`.
- Báo cáo cá nhân: `report/team/2A202603402_DoMinhHieu.md`.