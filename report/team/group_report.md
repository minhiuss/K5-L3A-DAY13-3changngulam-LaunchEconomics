# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: `3changngulam`
- Lớp: `L3A`
- Thành viên: xem `TEAM.md` (4 thành viên: Nguyễn Văn Nhi, Ngô Huy Hoàng, Nguyễn Ngọc Toàn, Đỗ Minh Hiếu)

## 2. Mục tiêu và cách tiếp cận

Dựng bộ hồ sơ **launch v0** cho trợ lý hoàn phí của LogiX-VN trên mẫu giả lập 1.200 yêu cầu (1.624 lần chạy) để trả lời bốn câu hỏi trước hội đồng **Gate 2a**: chi phí thật mỗi việc thành công so với nhân viên tự làm (`12.000 đ`), yếu tố nhạy cảm và rủi ro kinh tế, phân loại và khắc phục 20 ca lỗi, cùng kế hoạch pilot tách được tác động và đủ cỡ mẫu. Nhóm chia vai chạy code, kiểm số đối chiếu, gắn nhãn độc lập, giữ hồ sơ và hợp nhất các nhánh về `main`.

## 3. Giải pháp

- **Nhiệm vụ A (CP1 — Mô hình chi phí):** Hiện thực 3 hàm kinh tế chạy lại A1, hàm `mo_hinh` cộng mọi lần chạy (kể cả lỗi) chia cho số việc thành công (`978`), tách theo 4 loại yêu cầu (A3) và cộng chi phí cố định 40 triệu đ/tháng (A4) trong [src/lab13.py](../../src/lab13.py) và [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (CP2 — Độ nhạy):** Gọi lại `mo_hinh` cho 9 kịch bản đơn biến (B1), 1 kịch bản đôi (B2), so sánh giới hạn 1–2–3 lần chạy cả hệ thống (B3) và xem lại 100% ở hai mức làm lại `9 phút` và `15,3 phút` (B4) trong [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (CP3 — Bảng lỗi):** Hai lượt gắn nhãn độc lập 20 ca theo 5 loại Google PAIR đạt đồng thuận `100%` (`20/20`) và xây dựng bảng phát hiện/khắc phục cho 5 ca đại diện (`1, 20, 3, 19, 12`) trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (CP4 — Kế hoạch pilot):** Tính 5 câu D1, chọn chia theo nhân viên `20 + 20` phân tầng theo depot, đánh giá power, tính số nền và hoàn thiện đủ 3 luật dừng `NẾU – TRONG – THÌ – KHÔNG THÌ` trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (CP5 — Chỉ số, rủi ro & Hồ sơ Gate 2a):** Đặc tả 5 chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế trong [chi_so.md](chi_so.md); tổng hợp hồ sơ một trang trong [ho_so_launch_v0.md](ho_so_launch_v0.md); chấm chéo nhóm bạn trong [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Chi phí thật & phạm vi:** Toàn mẫu đạt **4.472 đ/việc thành công** (`simulated`), gấp **16,3×** hoá đơn token + tool (`274,7 đ/yc`); giờ nhân viên chiếm **92,5%** (`51,8%` làm lại, `40,7%` xem lại, `simulated`). Chi phí cả hệ thống là **5.865 đ/yc (`0,49×`)** (`simulated`). Thu hẹp phạm vi pilot về **`noi_dia` + `hang_nang`** cho chi phí **4.599 đ/việc (`0,38×`)** đã gồm cố định `40 triệu đ/tháng` ở `45.000 yc/tháng` (`5.784 đ = 0,48×` ở nửa khối lượng, `simulated`); loại `quoc_te` (`22.515 đ = 1,88×`, `simulated`) và `doi_tac` (`10.215 đ = 0,85×`, `simulated`).
- **Độ nhạy & số bất lợi:** Yếu tố nhạy nhất là **số ca làm lại** (`+51,8%` nếu gấp đôi), rồi **tỉ lệ xem lại** (`+40,7%`) và **lương nhân viên** (`+23,1%` khi tăng 25%) (`simulated`). Giới hạn **2 lần chạy** cho chi phí hệ thống thấp nhất (**6.901.220 đ**, `simulated`). Tuy nhiên, nếu phải xem lại 100% trong phạm vi thì chi phí lên **11.743 đ (`0,98×`)** với `9 phút` làm lại hoặc **12.415 đ (`1,03×`)** với `15,3 phút` đo từ mẫu (`simulated`).
- **Chỉ số đợt chạy thử (chưa có đối chứng) & Pilot:** Chỉ số chính trong đợt chạy thử là **82,83%** (`994/1.200`; phạm vi pilot `92,26%`), bỏ qua gợi ý **27,12%** (`21,09%` phạm vi), mở lại 7 ngày **4,25%** (`3,97%` phạm vi). Pilot chia `20 + 20` nhân viên với **MDE = 6 điểm** (`n = 859/nhóm`, `m ≥ 299 yc/người`, `DE = 6,96`), chấp nhận power còn **0,64** nếu tác động thật là 5 điểm.
- **Đề xuất Gate 2a (`ho_so_launch_v0.md`):** **Go có điều kiện** cho pilot `noi_dia` + `hang_nang` (4 điều kiện gắn rõ người phụ trách và ngày kiểm tra).
- **Duyệt chéo tại hội đồng (`phieu_cham.md`):** Nhóm `3changngulam` đóng vai hội đồng chấm hồ sơ nhóm `XinCaiTen` (L3A) đạt **26/30 điểm** (quyết định `Go có điều kiện`).

## 5. Khó khăn và cách xử lý

- **Không đủ cụm ở mức chênh 5 điểm:** 40 nhân viên chỉ đạt trần hiệu dụng `1.000 < 1.251`. Nhóm chuyển sang MDE `6 điểm`, ghi rõ đánh đổi power `0,64` và yêu cầu Giám đốc vận hành ký chấp nhận.
- **Rủi ro từ giờ nhân viên giả lập:** Hai cột `_simulated` chiếm `92,5%` tổng chi phí và có thể khiến xem lại 100% đắt hơn tự làm (`1,03×`, `simulated`). Nhóm gắn nhãn `simulated` ở mọi số liên quan và đặt điều kiện đo phút thật ngay từ tuần đầu qua 10 event có `trace_id`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và bốn báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- **Chưa có phút xem lại/làm lại đo thật và chưa có nhóm đối chứng:** Cần bật đủ 10 event có `trace_id`, hiệu chỉnh lại mô hình chi phí sau tuần 1 và chỉ đánh giá tác động tại bước `0.50` có nhóm đối chứng đồng thời.
- **Lớp an toàn sổ cái:** Cần hoàn tất khoá chống trùng `idempotency_key` và đối soát sổ cái mỗi giờ trước ngày chạy pilot `2026-12-07`.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`statsmodels.stats.power`)
- Tài liệu nội bộ lab: [docs/du_lieu_va_cong_thuc.md](../../docs/du_lieu_va_cong_thuc.md), [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
