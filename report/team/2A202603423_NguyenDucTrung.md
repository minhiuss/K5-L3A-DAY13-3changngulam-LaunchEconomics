# Báo cáo cá nhân — NguyenDucTrung-2A202603423

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Trung
- MSSV: 2A202603423
- Email: trungducnguyen2k@gmail.com
- Vai trong nhóm: Phụ trách CP5 (chỉ số, event, rủi ro kinh tế, hồ sơ launch v0)

## 2. Phần việc phụ trách

- Phụ trách **CP5 (Nhiệm vụ E: Chỉ số, event, rủi ro kinh tế, hồ sơ launch v0 — E1, E2, E3)**.
- Phối hợp tổng hợp các kết quả từ CP1 (mô hình chi phí), CP2 (bảng độ nhạy), CP3 (bảng lỗi Google PAIR), CP4 (kế hoạch pilot), hoàn thiện `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` và đóng góp vào `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- **Nhiệm vụ E1 (Chỉ số và Event):**
  - Tính toán 3 chỉ số chính trên 1.200 yêu cầu trong `src/lab13.py`: chỉ số chính (đóng trong 24 giờ và không mở lại trong 7 ngày) đạt `82,83%` trên toàn mẫu (994/1.200) và `92,26%` trong phạm vi pilot `noi_dia` + `hang_nang` (906/982); chỉ số mức dùng (bỏ qua gợi ý `sua` + `bo`) đạt `27,12%` (48/177 ca được xem lại) và `21,09%` (27/128) trong phạm vi; chỉ số an toàn (lỗi lọt đến khách, mở lại trong 7 ngày) đạt `4,25%` (51/1.200) toàn mẫu và `3,97%` (39/982) trong phạm vi.
  - Đề xuất thêm 2 chỉ số: chỉ số dùng (% yêu cầu nhóm can thiệp mở bằng trợ lý) và chỉ số an toàn (% đơn hoàn sai tiền phát hiện qua kiểm tra mẫu hàng tuần).
  - Thiết kế danh mục 10 event nghiệp vụ bắt buộc mang `trace_id` (`refund_request_created`, `agent_run_completed`, `agent_suggestion_shown`, `staff_review_decision`, `staff_rework_completed`, `refund_ledger_write`, `handoff_to_staff`, `ticket_closed`, `ticket_reopened`, `audit_sample_checked`) cùng bảng kiểm tra chéo đảm bảo mọi chỉ số đều đo lường được từ event.
- **Nhiệm vụ E2 (Rủi ro kinh tế — Risk Register):**
  - Trích xuất 4 dòng rủi ro kinh tế then chốt từ bảng độ nhạy B1/B2 với số liệu cụ thể kèm nhãn `simulated`: (1) Số ca làm lại tăng gấp đôi (+51,8%, lên 6.787 đ [simulated]); (2) Xem lại 100% kéo dài qua tuần đầu (11.743 đ = 0,98× con người, hầu như không tiết kiệm); (3) Lương nhân viên tăng 25% (+23,1%, lên 5.506 đ); (4) Mở phạm vi sang `quoc_te` (22.515 đ = 1,88× con người, thành công chỉ 27,3%).
  - Gán dấu hiệu theo dõi, hành động ứng phó cụ thể và một vai trò phụ trách duy nhất cho từng rủi ro (PM trợ lý hoàn phí, Trưởng nhóm CSKH, Kế toán trưởng, Giám đốc vận hành).
- **Nhiệm vụ E3 (Hồ sơ launch v0):**
  - Hoàn thiện trang hồ sơ 7 mục theo chuẩn Gate 2a, mỗi mục có con số chính, trạng thái minh bạch ("Giả lập" cho các mục tính từ `_simulated`, "Xong, có bằng chứng" cho các mục khác), người phụ trách là một vai trò cụ thể (không ghi "cả đội").
  - Xây dựng đề xuất **Go có điều kiện** kèm 5 điều kiện tiên quyết có người phụ trách và ngày kiểm tra cụ thể. Đảm bảo tuân thủ nghiêm ngặt quy định Gate 2a chỉ duyệt thử nghiệm pilot.

## 4. Bằng chứng

- Nhánh làm việc riêng: `cp5-trung` (dựa trên `main`).
- Code: Khối in chỉ số E1/D3 trong `src/lab13.py`.
- Hồ sơ: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`, `report/team/2A202603423_NguyenDucTrung.md`.
- Kết quả chạy `cd src && python lab13.py`: Khối `E1/D3` in đúng:
  - Toàn bộ 1.200 yc: đóng 24h không mở lại `82.83%` (994/1200), mở lại 7 ngày `4.25%` (51/1200), bỏ qua gợi ý `27.12%` (48/177 ca xem lại).
  - Phạm vi noi_dia + hang_nang: đóng 24h không mở lại `92.26%` (906/982), mở lại 7 ngày `3.97%` (39/982), bỏ qua gợi ý `21.09%` (27/128 ca xem lại).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI Antigravity (Gemini).
- **Mục đích:** Hỗ trợ rà soát yêu cầu đề bài CP5, thiết kế bảng ma trận event - chỉ số, kiểm tra tính nhất quán của các con số rủi ro kinh tế giữa `bang_chi_phi.md` và `chi_so.md`, rà soát từ cấm và quy tắc nhãn `simulated`.
- **Cách tự kiểm tra:**
  - Chạy script kiểm tra đầu ra trong `src/lab13.py` (sai số 0% so với slide đáp án).
  - Dùng regex rà soát không có biểu tượng/icon lạ, kiểm tra không có từ cấm trong hồ sơ Gate 2a.

## 6. Tự đánh giá

- Hoàn thành đầy đủ các yêu cầu của CP5 (E1, E2, E3), dữ liệu khớp 100% với đề bài và quy định của Gate 2a.
