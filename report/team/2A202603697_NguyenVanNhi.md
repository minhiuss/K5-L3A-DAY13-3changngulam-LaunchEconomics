# Báo cáo cá nhân — NguyenVanNhi-2A202603697

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Nhi
- MSSV: 2A202603697
- Email: nguyenvannhi224@gmail.com
- Vai trong nhóm: Người viết code (phụ trách CP1)

## 2. Phần việc phụ trách

- Phụ trách **CP1 (Nhiệm vụ A: Mô hình chi phí mỗi việc thành công — A1, A2, A3, A4)**.
- Triển khai code chuẩn trong `src/lab13.py` (thiết kế sẵn tham số ở hàm `mo_hinh` để CP2 tái sử dụng), hoàn thiện phần A1–A4 trong `report/team/bang_chi_phi.md`, và hỗ trợ tổng hợp phần **CP5** (`report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`) cho cả nhóm.

## 3. Đóng góp cụ thể

- **Nhiệm vụ A1:** Hiện thực 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` trong `src/lab13.py` và kiểm chứng qua `kiem_tra_dap_an_biet_truoc()` (`1,20` · `1,25` · `1,25`).
- **Nhiệm vụ A2:** Hiện thực `mo_hinh(runs, reqs, ...)` tính chi phí từ `logix_runs.csv` (1.624 lần chạy) và `logix_requests.csv` (1.200 yêu cầu, đọc với `keep_default_na=False`), hỗ trợ đầy đủ tham số `gia_*`, `luong_phut`, `he_so_*`, `max_lan_chay` cho CP2.
- **Nhiệm vụ A3 & A4:** Hiện thực `in_nhiem_vu_a(runs, reqs)` tách chi phí theo 4 loại yêu cầu (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`), tính bảng tỉ lệ `status == 'ok'` theo từng `attempt`, và tính chi phí cố định 40 triệu đ/tháng cho phạm vi pilot `noi_dia` + `hang_nang` ở mức 45.000 và 22.500 yêu cầu/tháng.
- **Hồ sơ nhóm & tổng hợp CP5:** Điền bảng A1–A4 trong `report/team/bang_chi_phi.md`; bổ sung tính chỉ số chính E1 vào `src/lab13.py` (`82,83%` toàn mẫu, `92,26%` trong phạm vi); tổng hợp số liệu CP1–CP4 hoàn thiện `report/team/chi_so.md` (5 chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế), `report/team/ho_so_launch_v0.md` (7 mục + đề xuất `Go có điều kiện`), `report/team/group_report.md` và cập nhật `TEAM.md`.

## 4. Bằng chứng

- Nhánh làm việc riêng: `cp1` (đã hợp nhất vào `main` qua PR #1) và đóng góp tổng hợp CP5 trên `main`.
- File đã thực hiện: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`, `report/team/2A202603697_NguyenVanNhi.md`.
- Kết quả chạy `cd src && python lab13.py`:
  - `Ba phép thử đáp án biết trước: ĐẠT` (`1.20`, `1.25`, `1.25`).
  - **A2:** Token `245.585 đ`, Tool `84.000 đ` (5.600 lần gọi), Lần chạy 2 & 3 `93.804 đ`, Xem lại `1.780.000 đ` (`simulated`), Làm lại `2.264.000 đ` (`simulated`), Tổng `4.373.585 đ` (`simulated`), Thành công `978`, CPS `4.472 đ` (`simulated`, gấp `16,3×` hoá đơn `274,7 đ`/yêu cầu), Chi phí hệ thống `5.865 đ`/yêu cầu (`0,49×`, `simulated`).
  - **A3:** `noi_dia` `2.696 đ` (`0,22×`, `simulated`), `hang_nang` `8.221 đ` (`0,69×`, `simulated`), `quoc_te` `22.515 đ` (`1,88×`, `simulated` — tỉ lệ `ok` giảm `30,0%` → `11,4%` → `2,2%`), `doi_tac` `10.215 đ` (`0,85×`, `simulated`).
  - **A4:** Trong phạm vi `noi_dia` + `hang_nang`, tổng chi phí mỗi việc thành công khi cộng cố định 40 triệu đ/tháng là `4.599 đ` (`0,38×`, `simulated`) ở mức 45.000 yc/tháng và `5.784 đ` (`0,48×`, `simulated`) ở một nửa khối lượng.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI Antigravity (Gemini).
- **Mục đích:** Hỗ trợ đọc nhanh cấu trúc repo và yêu cầu đề bài, gợi ý cấu trúc code cho `src/lab13.py`, định dạng bảng báo cáo và kiểm tra điều kiện nghiệm thu CP1.
- **Cách tự kiểm tra:**
  - Chạy trực tiếp `python lab13.py` trong `src/` kiểm tra 3 phép thử A1 đạt `1,20 · 1,25 · 1,25`.
  - Đối chiếu toàn bộ số liệu đầu ra với công thức gốc trong `docs/du_lieu_va_cong_thuc.md` và bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai số 0%).
  - Kiểm tra mọi con số từ hai cột `_simulated` đều có nhãn `simulated`, câu trả lời ≤ 3 dòng và không chứa từ cấm.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ và đầy đủ các yêu cầu của CP1 (A1–A4), dữ liệu khớp 100% đáp án chuẩn và sẵn sàng để các thành viên khác kế thừa hàm `mo_hinh` cho CP2.
