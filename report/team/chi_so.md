# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (`994 / 1.200`; trong phạm vi `noi_dia` + `hang_nang`: **92,26%**, `906 / 982`) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại (`duoc_xem_lai == 1`) | Chỉ số trong đợt chạy thử là **27,12%** (`48 / 177`; trong phạm vi `noi_dia` + `hang_nang`: **21,09%**, `27 / 128`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (`51 / 1.200`; trong phạm vi `noi_dia` + `hang_nang`: **3,97%**, `39 / 982`) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp có gợi ý trợ lý được mở xem trên giao diện | Số yêu cầu nhóm can thiệp có event `agent_suggestion_shown` chia tổng số yêu cầu nhóm can thiệp (`arm == 'treatment'`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền hoặc hoàn trùng qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm ca 5, 17 và hệ thống ca 7, 20) | Số đơn có `so_tien_da_hoan != so_tien_dung` trong `audit_sample_checked` chia tổng số đơn kiểm tra mẫu (`100 đơn/tuần`) | Không cần tính |

Chỉ số trong đợt chạy thử là **82,83%** (`994 / 1.200`; trong phạm vi `noi_dia` + `hang_nang` là **92,26%**, `906 / 982`). Nhóm không viết "trợ lý đã nâng chỉ số từ baseline `0,70`" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event (tối thiểu 6), mỗi event đều mang `trace_id` để nối với trace của agent và khớp với hệ thống theo dõi lỗi trong `bang_loi.md`.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id, order_id, depot, loai, so_tien_vnd, arm, created_at, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `run_id, request_id, attempt, tokens_in, tokens_out, tool_calls, status, missing_fields, trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id, staff_id, so_tien_de_xuat, price_table_version, trace_id` | Khi gợi ý của trợ lý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id, staff_id, quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id, staff_id, phut_lam_lai` (đo thật), `ly_do_lam_lai, trace_id` | Khi nhân viên hoàn tất làm lại ca trả lời sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id, order_id, fee_type, idempotency_key, transaction_id, so_tien, dich_hoan, bank_error_code, ket_qua, trace_id` | Khi ghi nhận giao dịch hoàn phí vào sổ cái |
| `handoff_to_staff` | Agent | `request_id, reason` (`thieu_du_lieu`/`qua_12_thang`/`loi_3_lan`), `tom_tat, trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id, closed_at, ket_qua, trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách / Hệ thống ticket | `request_id, reopened_at, reason` (`chua_nhan_tien`/`sai_so_tien`/...), `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán | `request_id, order_id, so_tien_da_hoan, so_tien_dung, price_table_version, trace_id` | Hằng tuần khi kiểm tra mẫu 100 đơn so với bảng giá |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (`% đóng trong 24h và không mở lại trong 7 ngày`):** nối theo `trace_id` từ `refund_request_created` (`created_at`), `ticket_closed` (`closed_at <= created_at + 24h`) và không phát sinh `ticket_reopened` trong 7 ngày sau `closed_at`.
- **Chỉ số dùng (`Tỉ lệ bỏ qua gợi ý`):** tính từ `staff_review_decision` (số event có `quyet_dinh_xem_lai` là `sua` hoặc `bo` chia tổng số event `staff_review_decision`).
- **Chỉ số an toàn (`Tỉ lệ lỗi lọt đến khách`):** đếm số `request_id` có `ticket_reopened` trong 7 ngày từ `ticket_closed`, chia tổng số `refund_request_created`.
- **Chỉ số dùng tự đề xuất (`% yêu cầu nhóm can thiệp mở gợi ý`):** đếm số `request_id` có `agent_suggestion_shown` chia số `refund_request_created` có `arm == 'treatment'`.
- **Chỉ số an toàn tự đề xuất (`% đơn hoàn sai tiền qua kiểm tra mẫu` & phát hiện hoàn trùng):** tính từ `audit_sample_checked` (tỉ lệ `so_tien_da_hoan != so_tien_dung`) và đối soát mỗi giờ `refund_ledger_write` theo mã đơn + khoản phí.

## E2 · Rủi ro kinh tế

Số lấy trực tiếp từ bảng độ nhạy (`bang_chi_phi.md`). Mọi con số dựa trên hai cột `_simulated` đều gắn nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, từ `4.472 đ` lên **6.787 đ** (`simulated`) | Tỉ lệ ca làm lại theo tuần `> 7%` (đợt chạy thử là `4,89%` = `48/982` trong phạm vi `noi_dia` + `hang_nang`) đo từ `staff_rework_completed` | Thu hẹp phạm vi về `noi_dia`, giới hạn tối đa `2 lần chạy`, rà `20 trace` làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Trong phạm vi `noi_dia` + `hang_nang`: CPS lên **11.743 đ (`0,98×`)** với `9 phút/ca` làm lại hoặc **12.415 đ (`1,03×`)** với `15,3 phút/ca` đo từ mẫu (`simulated`, vượt `12.000 đ`) | Tỉ lệ yêu cầu phải xem lại còn `> 50%` ở cuối bước rollout `0.25` hoặc thời gian xem lại trung bình `> 4,8 phút/ca` từ `staff_review_decision` | Giảm tỉ lệ xem lại theo bậc cho `noi_dia` khi `sua + bo < 15%`; tối ưu màn hình duyệt để giữ `≤ 4,8 phút/ca` | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến (gánh cố định 40 triệu đ/tháng) | Ở `45.000 yc/tháng`: `+1.185 đ/việc` → **4.599 đ (`0,38×`)**; giảm một nửa còn `22.500 yc/tháng`: cố định gấp đôi lên `+2.370 đ/việc` → **5.784 đ (`0,48×`)**; dưới `4.659 việc thành công/tháng` thì vượt `12.000 đ` (`simulated`) | Số việc thành công theo tuần trong phạm vi `< 50%` kế hoạch (`< 3.900 việc/tuần`) | Dừng mở rộng bước rollout tiếp theo và đàm phán lại gói chi phí cố định theo bậc sản lượng | PM trợ lý hoàn phí |
