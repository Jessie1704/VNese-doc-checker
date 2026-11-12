# VNese-doc-checker

Bộ công cụ review và sửa diễn đạt tài liệu kỹ thuật tiếng Việt (hướng dẫn sử dụng, playbook, tài liệu kỹ thuật, quy trình phát triển phần mềm) cho bớt "giọng AI".

Nguyên tắc chính: sửa cách diễn đạt, không sửa nội dung. Giữ nguyên term tiếng Anh quen dùng trong nghề thay vì dịch gượng, viết câu ngắn, bỏ các cụm sáo.

## Cấu trúc

| Đường dẫn | Nội dung |
| --- | --- |
| `skills/viet-tai-lieu-ky-thuat-bot-giong-ai/SKILL.md` | Skill cho Claude: quy trình 6 bước, quy tắc thuật ngữ, quy tắc câu, bảng dấu hiệu giọng AI, checklist review |
| `examples/playbook-ai-dlc/md/` | Ví dụ: Playbook AWS AI-DLC đã sửa văn phong, mỗi chương một file Markdown |
| `examples/playbook-ai-dlc/playbook-ai-dlc.html` | Bản HTML đã xuất của playbook (mục lục bên trái, tìm kiếm, sáng/tối) |
| `examples/playbook-ai-dlc/tools/build.py` | Script ghép các file Markdown thành trang HTML |

## Dùng skill

- **Claude.ai:** nén thư mục `skills/viet-tai-lieu-ky-thuat-bot-giong-ai/` thành zip, rồi upload trong Settings, mục Skills.
- **Claude Code:** chép thư mục skill vào `~/.claude/skills/` để dùng cho mọi dự án, hoặc vào `.claude/skills/` trong repo để cả đội dùng chung.
- **Công cụ AI khác:** dán nội dung `SKILL.md` vào system prompt hoặc custom instructions.

Sau đó chỉ cần gửi tài liệu và nhờ review văn phong.

## Build lại bản HTML của ví dụ

```
pip install markdown
python examples/playbook-ai-dlc/tools/build.py <trang-mau.html> <output.html>
```

`<trang-mau.html>` là một trang HTML mẫu dùng làm khung. Script lấy stylesheet thứ hai và thẻ `<script>` cuối cùng của trang này.
