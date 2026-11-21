# Báo cáo cá nhân — DoMinhHieu-2A202603402

## 1. Thông tin thành viên

- Họ tên: Đỗ Minh Hiếu
- MSSV: 2A202603402
- Email: mhieudo11102@gmail.com
- Vai trong nhóm: phụ trách CP4 (Nhiệm vụ D · `pilot_plan.yaml`) và tạo, quản lý repo nhóm

## 2. Phần việc phụ trách

Em phụ trách Nhiệm vụ D: tính cỡ mẫu theo ba cách chia (D1), trả lời năm câu "tách được tác động" (D2) và viết kế hoạch pilot `report/team/pilot_plan.yaml` (D3). Em cũng tạo repo nhóm cho cả nhóm làm chung.

## 3. Đóng góp cụ thể

- **Repo nhóm:** fork repo đề, đồng bộ lại khi repo đề đổi cấu trúc, đổi tên theo mẫu.
- **D1 · Cỡ mẫu** (`src/lab13.py`, phần `TODO CP4`):
  - Viết hàm `co_mau(p1, p2)` theo công thức so sánh hai tỉ lệ trong hướng dẫn, dùng `statistics.NormalDist`; đối chiếu chéo bằng `statsmodels` (1.250, lệch 0,1%).
  - Tính năm câu a–e: chia theo yêu cầu `1.251`/nhóm; theo nhân viên m = 75 thì DE `2,48` → `3.103`/nhóm → 42 người/nhóm, cần 84 > 40 nên không đủ người; 20 người/nhóm tối đa `1.000` < 1.251; 6 depot tối đa `300`; mức chênh 6 điểm cần `859`/nhóm → mỗi người ≥ `299` yêu cầu, DE `6,96`.
  - Tính con số bất lợi: nếu tác động thật chỉ 5 điểm thì power với n = 859 chỉ còn `0,64` (`NormalIndPower().power`).
- **D2:** chọn chia theo nhân viên 20 + 20 và trả lời năm câu kiểm tra tách được tác động, ghi vào chú thích đầu `pilot_plan.yaml`.
- **D3:** thêm đoạn code tính số nền trước khi đặt luật dừng: mở lại 7 ngày `4,25%` (toàn bộ), `3,97%` (phạm vi `noi_dia` + `hang_nang`); bỏ qua gợi ý `27,12%` / `21,09%`. Điền đầy đủ `pilot_plan.yaml`: owner, phạm vi theo kết quả A3, mde 0,06, ba luật dừng (an toàn, chi phí, sử dụng) đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ, lịch rollout, ngày quyết định, các số simulated.


## 4. Bằng chứng

- Commit `edce320`: D1 cỡ mẫu (`co_mau`, câu a–e) và kết quả D1 trong `pilot_plan.yaml`.
- Commit `671f570`: power 0,64, D2, D3 `pilot_plan.yaml`, số nền mở lại / bỏ qua gợi ý.
- `src/lab13.py`: hàm `co_mau` và khối `TODO CP4` (in các dòng `D1a`…`D1e`, `D1 power`, `D3`).
- `report/team/pilot_plan.yaml`: đọc được bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích, có 3 luật dừng.

## 5. Công cụ AI đã dùng

Dùng **Claude Code** làm trợ giảng trong lúc làm CP4:

- **Giải thích khái niệm:** cỡ mẫu, hệ số thiết kế, cỡ mẫu hiệu dụng khi chia theo cụm, power, ý nghĩa năm câu D2 (qua ví dụ so sánh hai lớp học).
- **Gợi ý code:** gợi ý dạng kế hoạch cho `co_mau` và câu b–d, sau đó em tự viết. Câu e em làm sai hai lần (bỏ mất kết quả `co_mau(0.70, 0.76)` và dùng nhầm công thức cỡ mẫu hiệu dụng thay cho mục tiêu 859), nên đã xem đáp án kèm giải thích của AI rồi sửa lại. AI cũng giúp sửa lỗi đặt `def co_mau` bên trong `if __name__ == '__main__'` (gây `ImportError`).
- **D3:** nhờ AI soạn các trường của `pilot_plan.yaml` dựa trên số của nhóm (A3, B, D1); đọc lại từng trường cùng phần giải thích của AI.
- **Repo:** AI giúp đồng bộ fork với repo đề, đổi tên repo và xử lý conflict khi rebase.

**Cách tự kiểm tra:**

- Chạy `python lab13.py` trong `src/` và đối chiếu từng dòng `D1a`…`D1e` với bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%).
- Thử `co_mau(0.5, 0.6)` = 388 trước khi tính số thật.
- Chạy `yaml.safe_load` và tìm dấu `?` ngoài dòng chú thích.
- Kiểm tra mỗi ngưỡng luật dừng nằm trên mức hiện tại (3,97% và 21,09%), để pilot không bị dừng ngay tuần đầu.

## 6. Tự đánh giá

- **Đã xong:** CP4 có đủ D1, D2, D3; các con số đều do `lab13.py` tính ra và khớp đáp án.
- **Điểm còn yếu:**
  - Phần cỡ mẫu khi chia theo cụm (câu e) và cách đọc kết quả power: em cần được giải thích nhiều lần mới hiểu.
  - Phần D3 do AI soạn, em đã đọc và hiểu ý chính nhưng cần ôn lại để tự giải thích được trước hội đồng (vì sao ngưỡng an toàn so với đối chứng thay vì 3% tuyệt đối, vì sao bước 0.50 kéo dài 3 tuần).
- **Lần sau:** viết hàm ở cấp ngoài cùng của file, lưu kết quả hàm vào biến trước khi dùng, và tự giải tay một ví dụ nhỏ trước khi viết code.
