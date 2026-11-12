---
name: "viet-tai-lieu-ky-thuat-bot-giong-ai"
description: "Review và sửa diễn đạt tài liệu kỹ thuật tiếng Việt (hướng dẫn, playbook, quy trình phần mềm) cho bớt giọng AI: giữ term tiếng Anh, câu ngắn, bỏ cụm sáo."
---

# Sửa tài liệu kỹ thuật tiếng Việt cho bớt giọng AI

Dùng khi người dùng đưa một tài liệu tiếng Việt về phát triển phần mềm (hướng dẫn sử dụng, playbook, tài liệu kỹ thuật, quy trình) và muốn sửa cách diễn đạt cho tự nhiên, bớt "giọng AI".

Mục tiêu: văn bản đọc như do một kỹ sư có kinh nghiệm viết cho đồng nghiệp: ngắn, rõ ai làm gì, dùng đúng thuật ngữ mà người trong nghề nói hằng ngày.

**Sửa diễn đạt, không sửa nội dung.** Chỗ nghi sai về kỹ thuật hoặc thiếu logic thì ghi chú cho tác giả, không tự sửa. Giữ nguyên tên riêng, mã văn bản (QT.IT.009...), số liệu, lệnh, đường dẫn file, link và trích dẫn nguồn. Không thêm nhận định mà bản gốc không có.

## Quy trình

1. **Lấy bản gốc.** File trên máy, link artifact, hoặc văn bản dán vào. Nếu artifact chỉ có PDF, dùng `pdftotext -layout` để lấy nội dung; bảng lớn thì trích bằng script rồi đối chiếu tổng (ví dụ số dòng, số ô đánh dấu) để chắc không sót.
2. **Quét nhanh cả tài liệu** và đếm các lỗi lặp lại (dấu "—", "không phải... mà...", "Đây là...", term bị dịch cứng, chú thích lặp, emoji). Báo số liệu này cho người dùng.
3. **Sửa thử một phần** (khoảng một chương hoặc 10–15 trang) dưới dạng bảng Trước / Sau / Lý do, gửi người dùng duyệt mức độ sửa và các term thay thế trước khi làm tiếp.
4. **Sửa toàn bộ** theo mức đã duyệt, mỗi chương một file Markdown để dễ sửa lại về sau.
5. **Xuất kết quả** theo định dạng người dùng muốn. Nếu cần trang HTML giống tài liệu mẫu của người dùng: dùng lại CSS và script (mục lục bên trái, tìm kiếm Ctrl+K, sáng/tối) của artifact mẫu, chuyển Markdown sang HTML, kiểm tra không còn link nội bộ hỏng và không tràn ngang ở độ rộng điện thoại. Lưu kèm bản Markdown nguồn vào thư mục dự án.
6. Chạy **checklist rà soát** ở cuối trước khi giao.

Nếu người dùng gửi tài liệu mẫu về giọng văn, đọc nó trước. Khi quy tắc dưới đây mâu thuẫn với cách viết trong mẫu, theo mẫu.

## Thuật ngữ

Giữ nguyên tiếng Anh những term mà dev, tester, BA vẫn nói hằng ngày. Phép thử: trong buổi họp team, mọi người nói từ nào thì viết từ đó.

- **Giữ tiếng Anh:** tên công cụ, tên vai trò, tên stage/phase, khái niệm kỹ thuật đặc thù, thao tác với code (merge, commit, deploy, build).
- **Chú thích một lần:** term ít gặp thì ghi nghĩa tiếng Việt trong ngoặc ở lần đầu, các lần sau dùng term gốc. Ví dụ "dependency DAG (đồ thị phụ thuộc)". Không lặp chú thích ở mỗi chương.
- **Dịch:** từ thông dụng đã có từ tiếng Việt quen thuộc (yêu cầu, kiểm thử, thiết kế, phạm vi, rủi ro, người duyệt).
- **Nhất quán:** mỗi khái niệm chỉ một cách gọi trong toàn tài liệu.

| Giữ tiếng Anh | Không dịch thành |
| --- | --- |
| merge, commit, pull request | hợp nhất, trộn, cam kết, yêu cầu kéo |
| code base, clone, worktree | cơ sở mã, bản sao mã |
| deploy, build, pipeline | triển khai bản dựng, đường ống |
| unit test, test case, regression | kiểm thử đơn vị, trường hợp kiểm thử, hồi quy |
| finding, artifact | phát hiện, tạo tác |
| approval gate, checkpoint | cổng phê chuẩn, điểm kiểm tra |
| walking skeleton, reverse engineering | bộ xương biết đi, kỹ thuật đảo ngược |
| API, schema, contract, interface | giao diện lập trình ứng dụng, lược đồ, hợp đồng |
| hash, deterministic, tombstone | băm, tất định, dấu mộ |
| Production, UAT, SIT | môi trường sản xuất |
| prompt, agent, workflow, model | lời nhắc, tác tử, luồng công việc, mô hình |
| tên phase/stage của công cụ (Inception...) | Khởi dựng... |

Với "ceremony" (các bước kiểm soát của quy trình), viết "mức độ kiểm soát" hoặc "số gate", không viết "nghi thức".

## Câu và đoạn

1. Câu ngắn, phần lớn dưới 25 từ. Câu dài thì tách, hoặc chuyển ý song song thành danh sách.
2. Chủ ngữ cụ thể: "Tech lead duyệt DAG", không "DAG sẽ được xem xét và phê duyệt". Hạn chế bị động.
3. Động từ trực tiếp: "duyệt" thay vì "tiến hành phê duyệt".
4. Câu đầu mỗi mục hoặc đoạn nói điểm chính.
5. Đoạn tối đa ba đến bốn câu. Đoạn là một quy tắc thì mở bằng cụm in đậm.
6. Nói lý do bằng hậu quả cụ thể, không bằng tính từ.
7. Giọng trung tính: không cảm thán, không khẩu hiệu. Viết hoa để nhấn chỉ dùng cho điều cấm ("KHÔNG tự merge").

## Dấu hiệu giọng AI cần sửa

Phần lớn cách sửa là bỏ bớt chữ.

| Dấu hiệu | Ví dụ | Cách sửa |
| --- | --- | --- |
| Dịch cứng term | "hợp nhất mã sau khi yêu cầu kéo được phê duyệt" | "merge code sau khi pull request được duyệt" |
| Cụm sáo | "đóng vai trò vô cùng quan trọng" | Nói hậu quả cụ thể, hoặc bỏ |
| "Không chỉ... mà còn...", "X, không phải Y" | dùng để nhấn mạnh | Chỉ giữ khi thật sự cần phân biệt hai khái niệm |
| "Đây là..." mở câu nhấn mạnh | "Đây là phân biệt quan trọng nhất của chương" | Bỏ, để nội dung tự nói |
| Danh từ hoá động từ | "tiến hành thực hiện việc kiểm tra" | "kiểm tra" |
| Câu mở đầu, câu tổng kết rỗng | "Trong bối cảnh...", "Tóm lại, việc tuân thủ...", "Một câu để nhớ:" | Bỏ, hoặc viết lại thành một câu có thông tin |
| Ẩn dụ, khẩu hiệu | "cỗ máy", "từ hư không", "trang giấy trắng", "đẻ ra", "Sinh ra là phải rà" | Nói thẳng nghĩa |
| Dịch nguyên văn thành ngữ tiếng Anh | "cư xử lạ", "khái niệm hạng nhất", "hỏng im lặng" | "hoạt động bất thường", "khái niệm cốt lõi", "lỗi không có cảnh báo" |
| Tính từ phóng đại | "toàn diện", "vượt trội", "liền mạch", "mạnh mẽ" | Số liệu cụ thể, hoặc bỏ |
| Bộ ba liệt kê cho đủ nhịp | "nhanh chóng, hiệu quả và chính xác" | Chỉ giữ ý có thật |
| Từ nối thừa | "Bên cạnh đó", "Ngoài ra", "Hơn nữa", "Nói cách khác" | Bỏ phần lớn |
| Giọng quá trang trọng | "Quý đồng nghiệp vui lòng tiến hành..." | "Dev cần..." hoặc câu mệnh lệnh trực tiếp |
| Rào đón mơ hồ | "trong một số trường hợp nhất định" | Nêu rõ trường hợp nào |
| Lạm dụng dấu "—" | "AI — công cụ mạnh mẽ — giúp..." | Dấu phẩy, dấu chấm, dấu hai chấm, hoặc tách câu. Giữ "—" trong text trích nguyên văn từ công cụ |
| Emoji trong callout | "🌱 Greenfield —" | Bỏ emoji, giữ chữ in đậm |

## Định dạng

- Tiêu đề: cụm danh từ ngắn, đánh số theo mục. Không dùng câu hỏi hay câu cảm thán.
- Danh sách đánh số cho các bước có thứ tự; mỗi bước mở bằng tên bước in đậm.
- Gạch đầu dòng cho ý song song. Không biến đoạn văn liền mạch thành gạch đầu dòng.
- Bảng khi so sánh nhiều mục theo cùng tiêu chí; ô bảng viết ngắn.
- Callout "Ghi chú", "Lưu ý", "Đề xuất" cho thông tin phụ, không cho nội dung chính.
- Checklist cho tiêu chí đạt ở các gate, mỗi dòng một điều kiện kiểm tra được.
- Tên file, lệnh, giá trị cấu hình đặt trong `code`.
- Sơ đồ ASCII giữ nguyên cấu trúc; chỉ sửa chữ bên trong cho khớp thuật ngữ.
- Không dùng emoji trong nội dung (trừ khi đang mô phỏng nguyên văn output của công cụ).

## Checklist rà soát trước khi giao

- [ ] Term kỹ thuật quen thuộc vẫn giữ tiếng Anh; term ít gặp có chú thích ở lần đầu, không lặp lại
- [ ] Mỗi khái niệm chỉ một cách gọi trong toàn tài liệu
- [ ] Không còn cụm trong bảng "Dấu hiệu giọng AI" (đếm lại bằng grep: "—", "trộn", "nghi thức", "Đây là", emoji)
- [ ] Câu đầu mỗi mục nói điểm chính; không có câu mở đầu hoặc tổng kết rỗng
- [ ] Mỗi việc có chủ thể rõ ràng
- [ ] Không đổi ý nghĩa kỹ thuật; chỗ nghi ngờ đã ghi chú cho tác giả
- [ ] Tên riêng, mã văn bản, số liệu, lệnh, đường dẫn và link giữ nguyên
- [ ] Link nội bộ không hỏng; bảng lớn đã đối chiếu tổng với bản gốc