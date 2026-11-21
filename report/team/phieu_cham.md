# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): 3changngulam (L3A)
- Nhóm được chấm: XinCaiTen (L3A) — repo `K5-L3A-DAY13-XinCaiTen-LaunchEconomics`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 8 | Đề xuất "Go có điều kiện" khớp số của nhóm và nêu được số bất lợi: xem lại 100% làm chi phí biến đổi lên 12.415 đ/việc (1,03× mức 12.000 đ) [simulated], power chỉ khoảng 64% nếu tác động thật là 5 điểm. Cách xử lý có: Giám đốc vận hành chấp nhận đánh đổi, đo phút thật, luật dừng chi phí 8.000 đ. Trừ điểm vì điều kiện Go chưa có ngày kiểm tra riêng; không có điều kiện sửa lỗi hoàn trùng/sổ cái; mục 5 hồ sơ ghi "Chưa" (bộ nhãn độc lập thứ hai còn thiếu) nhưng `bang_loi.md` ghi hai bộ nhãn trùng 20/20. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 9 | Mục 1, 2, 3, 7 của hồ sơ và `bang_chi_phi.md` đều gắn `simulated`; `pilot_plan.yaml` có mục `simulated_inputs`. Phạm vi thu hẹp về `noi_dia` + `hang_nang` có lý do bằng số: quoc_te 22.515 đ (1,88×), tỉ lệ thành công 27,3% [simulated]; doi_tac loại vì mẫu nhỏ (68 yêu cầu). Trừ nhẹ: cột "CPS biến đổi + cố định" ở bảng A4 chưa gắn nhãn ngay trong tiêu đề cột. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 9 | Chia theo nhân viên, ngẫu nhiên phân tầng theo depot, đối chứng đồng thời, đúng 20 cụm mỗi nhóm; cỡ mẫu 859 hiệu dụng/nhóm = 20 người × 299 yêu cầu (DE 6,96) cho chênh lệch 6 điểm. Ba luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng (mở lại +2 điểm hoặc >6%, CPS >8.000 đ trong 2 tuần, sử dụng <60% trong 7 ngày), người có quyền tắt là Giám đốc vận hành trong 30 phút, ngày quyết định 2027-01-05. Trừ nhẹ: ngưỡng sử dụng 60% chưa có căn cứ từ dữ liệu chạy thử. |
| **Tổng** | | | | **26 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Pilot `noi_dia` + `hang_nang` có đối chứng, đủ cỡ mẫu cho chênh lệch 6 điểm và luật dừng có ngưỡng; chi phí 4.599 đ/việc (0,38× mức 12.000 đ, đã gồm chi phí cố định) [simulated] ủng hộ chạy thử. Chưa thể Go hẳn vì xem lại 100% cho 12.415 đ (1,03×) [simulated], power chỉ khoảng 64% nếu tác động thật là 5 điểm, và còn thiếu bộ nhãn độc lập thứ hai ở bảng lỗi. Điều kiện cần có thêm: người phụ trách và ngày kiểm tra cho từng điều kiện, kế hoạch giảm xem lại theo bậc, sửa khóa chống trùng và đối soát sổ cái trước ngày bắt đầu.

**Một câu hỏi cho đội trình:** Nếu tuần đầu phải xem lại 100% thì chi phí là 12.415 đ/việc, cao hơn 12.000 đ nhưng luật dừng chi phí chỉ kích hoạt sau 2 tuần liên tiếp vượt 8.000 đ; nhóm xử lý khoảng hở này thế nào và ai có quyền dừng trong thời gian đó?
Theo kế hoạch hiện tại, PM trợ lý hoàn phí chỉ thu hẹp pilot khi chi phí vượt 8.000 đ/việc trong hai tuần liên tiếp. Giám đốc vận hành có quyền tắt trợ lý trong 30 phút theo luật an toàn. Kế hoạch chưa quy định ai được dừng vì chi phí ngay tuần đầu.

Nhóm có thể bổ sung một luật riêng: nếu chi phí đo được trong tuần đầu vượt 12.000 đ/việc thành công, PM đóng băng mở rộng ngay và trình Giám đốc vận hành quyết định tạm dừng pilot, chuyển yêu cầu về nhân viên. Giữ luật hai tuần ở ngưỡng 8.000 đ để xử lý chi phí cao kéo dài. Mức 12.415 đ là kịch bản mô phỏng, nên quyết định dừng cần dựa trên số đo thực tế của pilot.
