# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Hai lượt gắn nhãn dùng cùng 20 ca và năm định nghĩa từ đề Word. Hai bộ nhãn được ghi riêng rồi đối chiếu với nhau và với slide chữa.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** = 20 ca trùng ÷ 20 ca × 100% = **100%**. Bộ nhãn thống nhất khớp 20/20 ca với slide chữa.

## Quy tắc phân biệt cho các ca không trùng

Hai lượt cho cùng nhãn ở cả 20 ca. Xem ghi chú cuối bảng đối chiếu cho hai ca có thể lập luận theo cách khác.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Hằng ngày, lấy số lệnh bị ngân hàng từ chối vì sai số tài khoản chia cho số lệnh gửi ngân hàng, dựa trên `refund_ledger_write`. Cảnh báo khi vượt 1%. | Kiểm tra độ dài và định dạng theo ngân hàng trước khi tạo lệnh. Chỉ rõ trường cần sửa và cho khách xác nhận lại thông tin nhận tiền. | PM trợ lý hoàn phí |
| 20 | Hệ thống | Mỗi giờ, đối chiếu từng bản ghi `refund_ledger_write` thành công mới với lịch sử sổ cái theo mã đơn và khoản phí cần hoàn. Cảnh báo khi cùng một khoản có từ 2 mã giao dịch hoàn tiền khác nhau, kể cả khi khách dùng mã yêu cầu mới. | Dùng cùng `idempotency_key` cho cùng mã đơn và khoản phí. Sổ cái ghi tối đa một giao dịch thành công cho khóa đó và trả lại trạng thái lệnh cũ khi nhận lại yêu cầu. | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | Hằng tuần, lấy các yêu cầu đã ghi có vào ví và đã đủ 7 ngày theo dõi. Cảnh báo khi hơn 2% nhóm này có `ticket_reopened` vì `chua_nhan_tien` trong 7 ngày sau bản ghi `refund_ledger_write` thành công. | Báo trước tiền sẽ về ví LogiX trong 5 phút. Khi ghi có thành công, báo số tiền, nơi nhận và hướng dẫn rút về ngân hàng. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Hằng tuần, theo từng loại yêu cầu, tính tỉ lệ yêu cầu tạo trong tuần (`refund_request_created`) được chuyển với lý do `qua_12_thang` (`handoff_to_staff`). Cảnh báo khi vượt 5% để rà soát luồng chuyển. | Nêu rõ giới hạn tra cứu 12 tháng, chuyển nhân viên kèm mã đơn và tóm tắt, rồi báo khách thời gian phản hồi dự kiến. | PM trợ lý hoàn phí |
| 12 | Ngầm | Hằng ngày, cộng token của mọi lượt `agent_run_completed`, kể cả lượt lỗi, rồi tính token trung bình mỗi yêu cầu đã chạy theo depot. Cảnh báo khi một depot vượt 1,5 lần trung vị các depot và kiểm tra số lần gọi tool trong trace. | Kiểm tra trường bắt buộc trong phản hồi tool, ghi trường thiếu vào trace và chuyển nhân viên khi phản hồi thiếu dữ liệu để tránh gọi lặp. | Kỹ sư trưởng agent |

Các ngưỡng là đề xuất cho pilot. Dùng `trace_id` để nối các event. Ghi mã đơn, khoản phí, mã giao dịch, đích hoàn và mã lỗi ngân hàng tại sổ cái. Lấy loại yêu cầu và depot từ event tạo yêu cầu. Các trường này là đầu vào cho [danh sách event của CP5](chi_so.md).

<details>
<summary>Lý do gắn nhãn và nguồn đối chiếu cho 20 ca</summary>

| Ca | Nhãn tham khảo | Dấu hiệu quyết định |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu hai chữ số của tài khoản nhận tiền. |
| 2 | Hệ thống | Trợ lý tra bảng giá hàng thường cho kiện 28 kg, làm khoản hoàn thiếu 45.000 đ. |
| 3 | Ngữ cảnh | Tiền về ví LogiX đúng thiết kế, trong khi khách chờ tiền vào tài khoản ngân hàng. |
| 4 | Giới hạn hệ thống | LogiX thiếu dữ liệu của chặng do hãng nước ngoài giao. |
| 5 | Ngầm | Chỉ khi kiểm tra mẫu mới phát hiện 14 đơn được hoàn theo giá trước giảm. |
| 6 | Do người dùng | Khách chọn luồng giao trễ cho một yêu cầu về hàng bị vỡ. |
| 7 | Hệ thống | Trợ lý báo hoàn thành công dù sổ cái vẫn trả lỗi 503. |
| 8 | Hệ thống | Trích dẫn một điều khoản không tồn tại là sai sót nhìn thấy ngay trong câu trả lời. |
| 9 | Do người dùng | Khách nhập mã đơn của sàn vào trường cần mã vận đơn. |
| 10 | Ngữ cảnh | Điều khoản bất khả kháng được áp dụng đúng, nhưng cam kết 24 giờ trên ứng dụng tạo kỳ vọng khác. |
| 11 | Giới hạn hệ thống | Trợ lý chỉ xử lý được văn bản và khách gửi tin nhắn thoại. |
| 12 | Ngầm | Câu trả lời đúng che khuất chi phí token cao gấp 3 lần tại D05 suốt 3 tuần. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý. |
| 14 | Do người dùng | Khách bấm xác nhận đã nhận tiền khi tiền chưa về. |
| 15 | Hệ thống | Trợ lý tính hoàn 100% cho đơn trễ 26 giờ dù chính sách quy định 50%, và nhân viên phát hiện khi duyệt. |
| 16 | Ngữ cảnh | Gửi ngay lúc 2:14 sáng đúng thiết kế, nhưng giờ nhận thông báo làm phiền khách. |
| 17 | Ngầm | Bảng giá cũ làm lệch khoản hoàn của 212 đơn trong 9 ngày mà không có yêu cầu mở lại. |
| 18 | Ngữ cảnh | Khoản hoàn 15.000 đ đúng chính sách, nhưng thiếu cách tính khiến khách hiểu là hoàn thiếu. |
| 19 | Giới hạn hệ thống | Đơn đã 14 tháng, vượt phạm vi dữ liệu 12 tháng mà trợ lý tra được. |
| 20 | Hệ thống | Thiếu khóa chống trùng cho phép hai lệnh hoàn tiền cho cùng một đơn. |

Nguồn đối chiếu gồm [đề Word, mục Hai mươi ca lỗi](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx) và [slide chữa Nhiệm vụ C, trang 71](../../docs/Ngay13_Slide_Launch_Economics.pdf#page=71).

Slide 71 cũng chấp nhận nhãn **Hệ thống** cho ca 6 nếu nhóm lập luận rằng trợ lý phải đối chiếu mục đã chọn với mô tả, và cho ca 13 nếu nhóm tập trung vào việc trợ lý không nói rõ giới hạn của mình.

</details>
