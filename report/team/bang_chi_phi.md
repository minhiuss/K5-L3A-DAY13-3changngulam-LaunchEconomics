# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 (5.600 lần gọi) | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 (890 phút) | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 (1.132 phút) | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | cộng 4 khoản trên | simulated (có phần simulated) |
| Số việc thành công | 978 | `ket_qua` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | `4.373.585 ÷ 978` | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | `(245.585 + 84.000) ÷ 1.200` | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp **16,3 lần** (`4.472 đ` simulated so với `274,7 đ`). Nếu cộng thêm `222` ca không thành công do nhân viên làm thay (`12.000 đ/ca`), chi phí cả hệ thống là **5.865 đ/yêu cầu** (`0,49×` của `12.000 đ`, simulated).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** chiếm lớn nhất với **51,8%** (`2.264.000 đ`, simulated), tiếp theo là **xem lại 40,7%** (`1.780.000 đ`, simulated); tổng giờ nhân viên chiếm **92,5%** chi phí (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× (simulated) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× (simulated) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× (simulated) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× (simulated) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`** không đáng chạy (**22.515 đ = `1,88×`**, simulated, thành công **27,3%**); chạy lại 3 lần không giúp vì tỉ lệ `ok` giảm từ **30,0%** (lần 1) xuống **11,4%** (lần 2) và **2,2%** (lần 3). **`doi_tac`** (`10.215 đ = 0,85×`, simulated) có điều khoản riêng nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× (simulated) |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× (simulated) |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi kết luận ở quy mô `45.000` yc/tháng (`4.599 đ = 0,38×`, simulated) hay một nửa khối lượng (`5.784 đ = 0,48×`, simulated). Chi phí cố định `40 triệu đ/tháng` chỉ khiến trợ lý đắt hơn `12.000 đ` khi sản lượng dưới **4.659 việc thành công/tháng** (`< 6.212` yc/tháng, simulated).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (simulated) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (simulated) | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (simulated) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (simulated) | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (simulated) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (simulated) | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (simulated) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (simulated) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (simulated) | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi: **6.543 đ/việc thành công, tăng 46,3%** (simulated). Mức tăng bằng tổng tác động riêng `5,6% + 40,7%` do mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | **4.111 đ (simulated, thấp nhất)** |
| 2 lần | 4.093.220 đ (simulated) | 234 | **6.901.220 đ (simulated, rẻ nhất)** | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- **Hai lần** rẻ nhất cho cả công ty (`6.901.220 đ`, simulated), còn **một lần** có chi phí mỗi việc thành công thấp nhất (`4.111 đ`, simulated). Hai mục tiêu không trùng nhau vì giới hạn một lần đẩy thêm `85` yêu cầu sang nhân viên.

## B4 · Nếu phải xem lại tất cả

- Với `982` yêu cầu, xem lại `948` ca và làm lại `48` ca: dùng `9 phút/ca` cho chi phí **11.743 đ/việc = 0,98×**; dùng mức đo từ mẫu `15,3 phút/ca` thì thành **12.415 đ = 1,03×** (simulated).
- Xem lại 100% gần như không tiết kiệm. Pilot cần đo xem có thể giảm tỉ lệ xem lại an toàn không và giữ mỗi lần xem lại dưới **5,1 phút** (`9 phút` làm lại) hoặc **4,8 phút** (`15,3 phút` làm lại).
