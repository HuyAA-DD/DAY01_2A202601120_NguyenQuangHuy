# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 14h00–18h00
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.7, 1.2 và 1.8 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Hà Nội."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi? Ở mức nào phản hồi bắt đầu
kém mạch lạc?** (2–3 câu)
> *Qua bốn phản hồi, khi temperature tăng thì nội dung có xu hướng đa dạng hơn: từ Phố cổ 36 phố phường, Hồ Hoàn Kiếm, Con đường gốm sứ đến kỷ niệm 1000 năm Thăng Long. Tuy nhiên cả bốn phản hồi đều vẫn khá mạch lạc, đúng trọng tâm và không bị lan man rõ rệt. Với lần thử này, phản hồi ở mức 1.8 chưa kém mạch lạc, chỉ có vẻ rộng và diễn giải nhiều hơn một chút.*

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho trợ lý soạn thảo hợp đồng pháp lý,
và bao nhiêu cho trợ lý viết slogan quảng cáo? Giải thích khác biệt.**
> *Với trợ lý soạn thảo hợp đồng pháp lý, em sẽ đặt temperature thấp, khoảng 0.0 đến 0.2, vì cần câu trả lời ổn định, chính xác, ít sáng tạo tùy tiện và hạn chế diễn đạt mơ hồ. Với trợ lý viết slogan quảng cáo, em sẽ đặt temperature cao hơn, khoảng 0.8 đến 1.2, vì nhiệm vụ này cần nhiều ý tưởng mới, cách diễn đạt đa dạng và sáng tạo hơn. Khác biệt chính là hợp đồng pháp lý ưu tiên độ tin cậy và nhất quán, còn slogan quảng cáo ưu tiên sự mới mẻ và hấp dẫn.*

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 20.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 2 lần,
mỗi lần trung bình ~500 token đầu ra.

**Ước tính chi phí mỗi ngày của model lớn so với model nhỏ cho workload này
(dựa trên bảng giá trong template). Nêu một trường hợp model lớn xứng đáng
với chi phí và một trường hợp model nhỏ là lựa chọn đúng:**
> *Mỗi ngày có 20.000 x 2 = 40.000 lượt gọi API, mỗi lượt khoảng 500 token đầu ra, vậy tổng là khoảng 20.000.000 output token/ngày.Theo bảng giá trong template: gpt-4o có giá output $0.010 / 1K token, nên chi phí khoảng 20.000.000 / 1000 x 0.010 = $200/ngày. gpt-4o-mini có giá output $0.0006 / 1K token, nên chi phí khoảng 20.000.000 / 1000 x 0.0006 = $12/ngày.Model lớn xứng đáng khi tác vụ cần chất lượng cao, ví dụ phân tích pháp lý, tư vấn phức tạp hoặc xử lý yêu cầu quan trọng dễ gây hậu quả nếu sai. Model nhỏ là lựa chọn đúng cho các tác vụ số lượng lớn, rủi ro thấp như trả lời FAQ, tóm tắt ngắn, phân loại nội dung đơn giản hoặc gợi ý câu chữ cơ bản.*

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích máy học (machine learning) là gì?"** nhưng hai system prompt
khác nhau:
- "Bạn là một nhà thơ, trả lời mọi thứ bằng hình ảnh ví von, tránh thuật ngữ."
- "Bạn là kỹ sư phần mềm senior, trả lời chính xác, có ví dụ code khi phù hợp."

**Hai phản hồi khác nhau như thế nào (giọng văn, độ dài, mức kỹ thuật)?
Từ đó rút ra system prompt điều khiển được những khía cạnh nào của phản hồi?**
(3–4 câu)
> *Với persona “nhà thơ”, phản hồi thường mềm hơn, dùng nhiều hình ảnh ví von, ít thuật ngữ kỹ thuật và giải thích máy học theo kiểu dễ cảm nhận. Với persona “kỹ sư phần mềm senior”, phản hồi thường trực tiếp, chính xác hơn, có cấu trúc rõ và có thể dùng khái niệm kỹ thuật hoặc ví dụ code để minh họa. Như vậy, system prompt có thể điều khiển giọng văn, vai trò của mô hình, mức độ chuyên môn, cách diễn đạt, độ chi tiết và kiểu ví dụ được sử dụng. Nó không chỉ đổi “nội dung nói gì”, mà còn đổi “nói như ai” và “nói cho đối tượng nào”.*

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~150 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Nếu dùng ước lượng thô để dự
toán ngân sách API cho ứng dụng tiếng Việt, bạn sẽ dự toán thiếu hay thừa —
và vì sao?**
> *Với đoạn văn tiếng Việt mình thử có 133 từ. Cách ước lượng thô số từ / 0.75 cho ra khoảng 177 token, còn count_tokens bằng tiktoken cho ra 158 token, chênh khoảng 10.9%.Trong ví dụ này, ước lượng thô đang dự toán thừa so với số token thật, vì nó giả định trung bình 1 token chỉ tương đương 0.75 từ. Tuy nhiên với tiếng Việt, kết quả có thể dao động do dấu, khoảng trắng, từ ghép và cách tokenizer tách chữ; vì vậy dùng tiktoken sẽ đáng tin cậy hơn khi dự toán ngân sách API.*

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Xét ba ứng dụng: (a) chatbot văn bản, (b) trợ lý giọng nói đọc to phản hồi,
(c) pipeline dịch tài liệu chạy ngầm ban đêm. Ứng dụng nào hưởng lợi nhiều
nhất từ streaming, ứng dụng nào không cần — và tại sao?** (1 đoạn văn)
> *Chatbot văn bản hưởng lợi rất nhiều từ streaming vì người dùng nhìn thấy câu trả lời xuất hiện dần, cảm giác phản hồi nhanh hơn dù tổng thời gian sinh có thể không đổi. Trợ lý giọng nói cũng hưởng lợi, thậm chí rất rõ, vì có thể bắt đầu đọc phần đầu của câu trả lời trong khi phần sau vẫn đang được sinh, giúp cuộc hội thoại tự nhiên hơn và giảm thời gian chờ im lặng. Ngược lại, pipeline dịch tài liệu chạy ngầm ban đêm gần như không cần streaming, vì không có người dùng đang chờ từng token; điều quan trọng hơn là độ chính xác, hoàn tất ổn định, logging và xử lý lỗi.*

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**Khi API quá tải và hàng nghìn client cùng retry, exponential backoff giúp
gì so với delay cố định? Tra cứu thêm: kỹ thuật "jitter" (thêm độ trễ ngẫu
nhiên) giải quyết vấn đề gì còn sót lại?**
> *Exponential backoff giúp client chờ lâu dần giữa các lần retry, nên khi API quá tải sẽ giảm áp lực thay vì tiếp tục gửi lại dồn dập. Nhưng nếu nhiều client cùng retry theo cùng lịch, chúng vẫn có thể tạo spike mới. Jitter thêm độ trễ ngẫu nhiên để các retry được rải đều hơn, tránh hiện tượng nhiều client “đổ về” cùng lúc.*

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Viết lại system prompt bạn dùng cho trợ lý của mình. Chỉ ra 2 chỗ trong
prompt mà nếu xóa đi, hành vi trợ lý sẽ thay đổi rõ rệt — và mô tả thay đổi
đó:**
> *System prompt em dùng có thể là: “Bạn là trợ giảng AI thân thiện của khóa học, trả lời bằng tiếng Việt, ngắn gọn, dễ hiểu và ưu tiên ví dụ thực tế. Khi người học hỏi về code, hãy giải thích từng bước vừa đủ, chỉ ra lỗi thường gặp và đưa ví dụ chạy được.”Nếu xóa câu “trả lời bằng tiếng Việt”, trợ lý có thể chuyển sang tiếng Anh hoặc trộn ngôn ngữ, làm người học khó theo dõi hơn. Nếu xóa câu “ngắn gọn, dễ hiểu và ưu tiên ví dụ thực tế”, câu trả lời có thể dài hơn, lý thuyết hơn và ít gắn với bài tập cụ thể.*

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn giữ history 4 lượt cuối. Hãy mô tả một tình huống hội thoại
cụ thể mà giới hạn này khiến trợ lý trả lời sai/mất ngữ cảnh, và đề xuất một
cách khắc phục (ví dụ: tóm tắt các lượt cũ, tăng giới hạn có chọn lọc...):**
> *Ví dụ ban đầu người dùng nói app dùng FastAPI và PostgreSQL, nhưng sau nhiều lượt hỏi phụ, thông tin đó bị rơi khỏi 4 lượt history cuối. Khi người dùng hỏi “viết schema lưu lịch hẹn”, trợ lý có thể quên PostgreSQL và đề xuất thiết kế sai. Cách khắc phục: lưu bản tóm tắt ngắn các quyết định quan trọng ở các lượt cũ, rồi gửi kèm summary đó cùng 4 lượt gần nhất.*

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên GitHub cá nhân và nộp link repo vào vlearn (theo hướng dẫn README)
