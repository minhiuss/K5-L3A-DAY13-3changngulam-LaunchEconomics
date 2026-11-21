# Team

## Thông tin nhóm

- Tên nhóm: 3changngulam
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-3changngulam-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/minhiuss/K5-L3A-DAY13-3changngulam-LaunchEconomics

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Văn Nhi | 2A202603697 | nguyenvannhi224@gmail.com | hagasei | Người viết code (phụ trách CP1) |
|   2 | Ngô Huy Hoàng | 2A202603622 | — | HuyHoangg10 | Người kiểm số (phụ trách CP2) |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

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

- Người viết code — phụ trách CP1 (Nhiệm vụ A: Mô hình chi phí mỗi việc thành công)

### Đóng góp cụ thể

- Hiện thực 3 hàm kinh tế chạy lại ở A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), vượt qua 3 phép thử đáp án biết trước (`1,20` · `1,25` · `1,25`).
- Hiện thực hàm `mo_hinh(runs, reqs, ...)` ở A2 và hàm `in_nhiem_vu_a(runs, reqs)` tính chi phí từ trace (A2), tách theo 4 loại yêu cầu kèm tỉ lệ `status=ok` theo từng lần thử (A3), và tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4).
- Điền hoàn chỉnh kết quả và câu trả lời các mục A1, A2, A3, A4 (kèm nhãn `simulated` đầy đủ) vào `report/team/bang_chi_phi.md`.

### Bằng chứng

- Code: `src/lab13.py` (các hàm A1, `mo_hinh`, `in_nhiem_vu_a`).
- Hồ sơ: `report/team/bang_chi_phi.md` (các mục A1, A2, A3, A4).
- Báo cáo cá nhân: `report/team/2A202603697_NguyenVanNhi.md`.

## NgoHuyHoang-2A202603622

### Phần việc phụ trách

- Người kiểm số — phụ trách CP2 (Nhiệm vụ B: bảng độ nhạy).

### Đóng góp cụ thể

- Viết phần tính B1–B4 trong `src/lab13.py`, dùng lại hàm `mo_hinh()` của CP1 thay vì điền số cố định.
- Hoàn thiện 9 kịch bản B1, kịch bản kết hợp B2, so sánh giới hạn chạy lại B3 và trường hợp xem lại 100% ở B4.
- Điền kết quả CP2 vào `report/team/bang_chi_phi.md` và gắn nhãn `simulated` cho các số liên quan.

### Bằng chứng

- Code: `src/lab13.py` (`tinh_nhiem_vu_b`, `in_nhiem_vu_b`).
- Hồ sơ: `report/team/bang_chi_phi.md` (B1–B4).
- Báo cáo cá nhân: `report/team/2A202603622_NgoHuyHoang.md`.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
