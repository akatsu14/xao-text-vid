# Tra cứu nhân vật, kỹ năng và bài — Quốc Chiến 2.3.41.2

Trích từ các bảng dịch tiếng Việt của bộ game trên máy. Đây là mô tả dữ liệu, chưa đối chiếu toàn bộ với mã thực thi. Có cả gói mở rộng và gói bị tắt; có dữ liệu không đồng nghĩa nhân vật đang được phép chọn.

Tên nhân vật được nhận diện bằng mã tên có mục danh hiệu # tương ứng. Danh sách có thể không bao gồm những nhân vật không theo quy ước này. Kỹ năng được liệt kê riêng theo gói, không tự suy đoán kỹ năng thuộc nhân vật nào. Các mô tả tham chiếu bằng biểu thức Lua không phải chuỗi trực tiếp không được tự thực thi.

## BasaraMode

Nguồn: `lang\vi_VN\BasaraMode.lua`

### Huyết Chiến — `aozhan`


• Bạn không thể sử dụng [Đào] phi chuyển hóa
• [Đào] được chuyển hóa sử dụng/đánh ra thành [Sát]/[Thiểm].

### Châu Liên Hợp Bích — `companion`

Hạn định kỹ:
• Giai đoạn ra bài, bạn có thể rút 2 lá.
• Khi bạn cần sử dụng [Đào], bạn có thể xem như sử dụng [Đào].

### Âm Dương Ngư — `halfmaxhp`

Hạn định kỹ:
• Giai đoạn ra bài, bạn có thể rút 1 lá.
• Giai đoạn bỏ bài, bạn có thể lệnh giới hạn trữ bài của bạn +2.

### Tiên Khu — `firstshow`

Hạn định kỹ: Giai đoạn ra bài, bạn có thể bổ sung bài đến khi có 4 lá trên tay, sau đó xem 1 tướng ẩn của 1 người.

### Châu Liên Hợp Bích — `CompanionCard`

Tiêu Ký

Cách dùng 1:
Giai đoạn ra bài, bạn có thể loại bỏ Tiêu ký này, bạn rút 2 lá.

Cách dùng 2
Khi bạn cần sử dụng [Đào], bạn có thể loại bỏ Tiêu ký này, bạn xem như đã sử dụng [Đào].

### Âm Dương Ngư — `HalfMaxHpCard`

Tiêu Ký

Cách dùng 1:
Giai đoạn ra bài, bạn có thể loại bỏ Tiêu ký này, bạn rút 1 lá.

Cách dùng 2:
Giai đoạn bỏ bài, nếu bài trên tay lớn hơn giới hạn trữ bài, bài có thể loại bỏ Tiêu ký này, giới hạn trữ bài của bạn +2.

### Tiên Khu — `FirstShowCard`

Tiêu Ký

Giai đoạn ra bài, bạn có thể loại bỏ Tiêu ký này, bạn chọn 1 người có tướng chưa mở (bỏ qua nếu không có tướng nào chưa mở), bạn bổ sung bài trên tay tới 4 lá, sau đó bạn xem 1 tướng ẩn của người đã chọn.

### Dã Tâm Gia — `CareermanCard`

Tiêu Ký

Cách dùng 1:
Giai đoạn ra bài, có thể loại bỏ Tiêu ký này và chọn: 1. Rút 2 lá; 2. Rút 1 lá; 3. Rút bài đến khi tay có 4 lá và xem 1 tướng ẩn của người khác.

Cách dùng 2: Khi cần sử dụng [Đào], có thể loại bỏ Tiêu ký này, xem như đã sử dụng [Đào]

Cách dùng 3: Đầu giai đoạn bỏ bài, có thể loại bỏ Tiêu ký này, giới hạn trữ bài lượt này +2.

### Mở tướng — `showhead`

Mở Chủ tướng

### Mở tướng — `showdeputy`

Mở Phó tướng

## FormationPackage

Nguồn: `lang\vi_VN\Package\FormationPackage.lua`

Tên nhân vật nhận diện được: Đặng Ngải (`dengai`); Tào Hồng (`caohong`); Khương Duy (`jiangwei`); Tưởng Uyển & Phí Y (`jiangwanfeiyi`); Tưởng Khâm (`jiangqin`); Từ Thịnh (`xusheng`); Vu Cát (`yuji`); Hà Thái Hậu (`hetaihou`); Lưu Bị - Quân (`lord_liubei`).

### Đồn Điền — `tuntian`

• Sau khi bạn mất đi bài ngoài lượt, bạn có thể tiến hành phán xét, nếu kết quả phán xét không phải là chất CƠ, bạn có thể đặt kết quả phán xét này từ chồng bài bỏ lên tướng này, gọi là [Điền].
• Khoảng cách từ bạn tới người khác -X (X là số [Điền] bạn có).

### Cấp Tập — `jixi`

Chủ tướng kỹ, Giảm 0.5 máu gốc: Bạn có thể chuyển hóa sử dụng [Điền] thành [Thuận Thủ Khiên Dương].

### Tư Lương — `ziliang`

Phó tướng kỹ: Sau khi 1 người cùng thế lực với bạn nhận sát thương, bạn có thể giao cho họ 1 [Điền].

### Hộ Viện — `huyuan`

Khi bắt đầu giai đoạn kết thúc, bạn có thể chọn 1 mục:
1. Giao 1 lá phi trang bị cho 1 người;
2. Đặt 1 lá trang bị vào vùng trang bị của 1 người, sau đó bạn có thể bỏ 1 lá trên bàn chơi.

### Hạc Dực — `heyi`

Trận pháp kỹ: Quan hệ đội hình: Nếu bạn có trong quan hệ đội hình, người cùng đội hình với bạn nhận kỹ năng »Phi Ảnh«.

### Phi Ảnh — `feiying`

Tỏa định kỹ: Khoảng cách từ người khác đến bạn +1.

### Khiêu Hấn — `tiaoxin`

Một lần trong giai đoạn ra bài, bạn có thể lệnh 1 người có tầm đánh tới bạn chọn 1 mục:
1. Họ sử dụng [Sát] với bạn;
2. Lệnh bạn bỏ 1 lá của họ.

### Di Chí — `yizhi`

Phó tướng kỹ, Giảm 0.5 máu gốc: Nếu Chủ tướng của bạn:
* Có »Quan Tinh«: Số lá được xem luôn là 5;
* Không có »Quan Tinh«: Bạn nhận »Quan Tinh«.

### Thiên Phúc — `tianfu`

Chủ tướng kỹ, Trận pháp kỹ: Quan hệ đội hình: Trong lượt của người có trong quan hệ đội hình, bạn nhận kỹ năng »Khán Phá«.

### Sinh Tức — `shengxi`

Khi bắt đầu giai đoạn kết thúc, nếu trong lượt này bạn không gây sát thương, bạn có thể rút 2 lá.

### Thủ Thành — `shoucheng`

Sau khi người cùng thế lực với bạn mất đi lá cuối cùng trên tay họ nếu ở ngoài lượt của họ, bạn có thể lệnh họ rút 1 lá.

### Thượng Nghĩa — `shangyi`

Một lần trong giai đoạn ra bài, bạn có thể lệnh cho 1 người khác xem bài trên tay của bạn, sau đó bạn lựa chọn 1 mục:
1. Bạn xem bài trên tay họ và bỏ 1 lá màu Đen trong đó.
2. Bạn xem tất cả tướng ẩn của họ.

### Điểu Tường — `niaoxiang`

Trận pháp kỹ: Quan hệ vây công:
• Sau khi bạn xác định mục tiêu của [Sát], ứng với mỗi mục tiêu, nếu mục tiêu đó là người bên cạnh bạn và họ không nằm trong quan hệ đội hình, lệnh họ cần sử dụng 2 [Thiểm] để triệt tiêu [Sát] này.
• Nếu bạn là người vây công, sau khi người vây công xác định mục tiêu của lá [Sát], ứng với mỗi mục tiêu, nếu mục tiêu này là người bị vây công, lệnh họ cần sử dụng 2 [Thiểm] để triệt tiêu [Sát] này.

### Nghi Thành — `yicheng`

Sau khi người cùng đội hình với bạn xác định mục tiêu của [Sát] hoặc trở thành mục tiêu của [Sát], họ có thể rút 1 lá, sau đó bỏ 1 lá.

### Thiên Huyễn — `qianhuan`

• Sau khi 1 người cùng thế lực nhận sát thương, bạn có thể đem 1 lá của bạn đặt lên tướng này, gọi là [Huyễn] (Không thể đặt lá trùng chất với những [Huyễn] đã có).
• Khi 1 người cùng thế lực trở thành mục tiêu duy nhất của lá cơ bản/công cụ phổ thông, bạn có thể đưa 1 [Huyễn] vào chồng bài bỏ, hủy bỏ mục tiêu này.
• Khi có lá tiến vào vùng phán xét của người cùng thế lực với bạn, bạn có thể đưa 1 [Huyễn] vào chồng bài bỏ, đưa lá đó vào chồng bài bỏ.

### Độc Tửu — `zhendu`

Khi bắt đầu giai đoạn ra bài của người khác, bạn có thể bỏ 1 lá bài trên tay, nếu họ thỏa mãn điều kiện sử dụng [Tửu], thực hiện lần lượt:
- Họ xem như sử dụng [Tửu];
- Bạn gây 1 sát thương cho họ.

### Thích Loạn — `qiluan`

Khi kết thúc lượt của 1 người, nếu trong lượt này bạn đã giết người, bạn có thể rút 3 lá.

### Chương Vũ — `zhangwu`

Tỏa định kỹ:
• Khi [Phi Long Đoạt Phượng] tiến vào chồng bài bỏ hoặc vùng trang bị của người khác, bạn thu lấy nó.
• Khi bạn mất đi [Phi Long Đoạt Phượng] không vì sử dụng, bạn mở nó ra, đặt vào đáy chồng bài rút và bạn rút 2 lá.

### Thụ Việt — `shouyue`

Quân chủ kỹ, Tỏa định kỹ: Bạn có »Ngũ Hổ Tướng Đại Kỳ«.

»Ngũ Hổ Tướng Đại Kỳ«:
Người thuộc thế lực Thục thay đổi các kỹ năng sau:
* »Võ Thánh«: Thay đổi mô tả: Loại bỏ chữ "Đỏ".
* »Bào Hao«: Bổ sung mô tả: • Sau khi bạn xác định mục tiêu của lá [Sát], ứng với mỗi mục tiêu, bạn lệnh [Sát] này Bỏ qua phòng cụ của họ.
* »Long Đảm«: Bổ sung mô tả: • Khi bạn sử dụng hoặc đánh ra [Sát] hoặc [Thiểm] bởi phát động »Long Đảm«, bạn rút 1 lá.
* »Liệt Cung«: Bổ sung mô tả: • Tầm đánh của bạn +1.
* »Thiết Kỵ«: Thay đổi mô tả: "1 tướng đã mở" sửa thành "tất cả tướng đã mở".

### Kích Chiếu — `jizhao`

Hạn định kỹ: Khi bạn trong trạng thái hấp hối, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Bạn bổ sung bài trên tay đến giới hạn máu;
- Bạn hồi máu đến 2;
- Bạn mất kỹ năng »Thụ Việt« và nhận kỹ năng »Nhân Đức«.

### Phi Long Đoạt Phượng — `DragonPhoenix`

Bài Trang bị - Vũ khí

Tầm đánh: 2
Kỹ năng:
• Sau khi bạn xác định mục tiêu của [Sát], ứng với mỗi mục tiêu, bạn có thể lệnh họ bỏ 1 lá.
2. Khi mục tiêu của [Sát] do bạn sử dụng tiến vào trạng thái hấp hối bởi hiệu quả của [Sát] này, bạn có thể thu lấy 1 lá trên tay họ.

## HanPackage

Nguồn: `lang\vi_VN\Package\HanPackage.lua`

Tên nhân vật nhận diện được: Lưu Hiệp (`liuxie`); Lưu Biện (`liubian`); Trương Nhượng (`zhangrang`); Hà Tiến (`hejin`); Vương Doãn (`wangyun`); Vương Vinh (`wangrong`); Phục Hoàng Hậu (`fuhuanghou`); Phục Hoàn (`han_fuwan`); Đổng Thừa (`dongcheng`); Đường Cơ (`tangji`); Thái Ung (`caiyong`); Hoàng Phủ Tung (`huangfusong`); Lưu Hoành (`liuhong`).

### Thiên Mệnh — `tianming`

Sau khi bạn trở thành mục tiêu của [Sát], bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Bạn bỏ 2 lá trên tay;
- Bạn rút 2 lá.

### Mật Chiếu — `mizhao`

Một lần trong giai đoạn ra bài, bạn có thể giao X lá cho 1 người khác (X là số thế lực khác bạn trên bàn);
▷ Bạn lệnh họ đấu điểm với 1 người khác, người thắng xem như sử dụng 1 [Sát] với người thua.

### Thi Oán — `shiyuan`

Một lần trong lượt của mỗi người, sau khi bạn trở thành mục tiêu của bài do người khác sử dụng, nếu số máu của họ so với bạn:
* Lớn hơn: Bạn có thể rút 2 lá;
* Ngược lại: Bạn có thể rút 1 lá.

### Độc Thệ — `dushi`

Tỏa định kỹ:
• Người khác không thể sử dụng [Đào] với bạn.
• Khi bạn trận vong do người khác gay sát thương, họ nhận kỹ năng này.

### Thao Loạn — `taoluan`

Khi bạn cần sử dụng 1 lá cơ bản/công cụ phổ thông, bạn có thể mở tướng này, xem như sử dụng lá đó;
▶ Khi kết thúc lượt này, nếu bạn đã mở tất cả tướng, bạn chọn tối đa 3 người khác đã trở thành mục tiêu của lá đó và có bài trên tay, thực hiện lần lượt:
- Bạn lệnh họ mở 1 lá trên tay và giao cho bạn;
- Trong số những lá đã mở, nếu số lá màu Đỏ > màu Đen, bạn úp tướng này.

### Mưu Tru — `mouzhu`

Một lần trong giai đoạn ra bài, bạn có thể lựa chọn những người khác có số máu bằng bạn hoặc ở khoảng cách 1 của bạn, thực hiện lần lượt:
- Họ giao 1 lá trên tay cho bạn;
- Nếu số lá trên tay họ < bạn, họ có thể xem như sử dụng 1 [Sát] hoặc [Quyết Đấu] với bạn.

### Diên Họa — `yanhuo`

Khi bạn trận vong, bạn có thể chọn 1 mục:
1. Bạn bỏ X lá của nguồn sát thương;
2. Bạn bỏ 1 lá của tối đa X người;
(X là số lá trên tay bạn).

### Liên Kế — `lianji`

Giai đoạn ra bài, bạn có thể giao 1 lá trên tay cho 1 người khác chưa nhận bài từ kỹ năng này;
▶ Khi tính toán sát thương tiếp theo họ phải nhận trong lượt này, sát thương này +1.

### Định Trứ — `dingzhu`

Khi kết thúc giai đoạn ra bài, bạn có thể chọn 1 người khác đã nhận bài trong lượt này, họ xem như sử dụng 1 [Quyết Đấu].

### Mẫn Tư — `minsi`

Một lần trong giai đoạn ra bài, bạn có thể bỏ đi số lá tùy ý có tổng điểm bằng 13, sau đó lật ra số lá gấp đôi từ chồng bài rút, bạn thu lấy những lá đó;
▶ Những lá CƠ bạn đã thu bằng kỹ năng này trong lượt này không tính vào giới hạn trữ bài trên tay.

### Vũ Tụng — `wucong`

Khi bạn trận vong, bạn có thể lệnh 1 người khác có cùng thế lực với bạn nhận »Mẫn Tư«.

### Chúy Khủng — `zhuikong`

Khi bắt đầu giai đoạn chuẩn bị của người khác, nếu bạn đang bị thương, bạn có thể đấu điểm với họ:
* Nếu bạn thắng: Chặn tất cả sát thương họ gây ra trong lượt này;
* Nếu bạn không thắng: Họ có thể xem như sử dụng 1 [Sát] với bạn.

### Cầu Viện — `qiuyuan`

Khi bạn trở thành mục tiêu của [Sát], bạn có thể lệnh 1 người khác ngoài người sử dụng chọn 1 mục:
1. Họ giao cho bạn 1 lá [Thiểm];
2. Họ trở thành mục tiêu của [Sát] này.

### Thừa Chiếu — `chengzhao`

Khi bắt đầu giai đoạn kết thúc của 1 người, nếu lượt này bạn đã nhận từ 2 lá trở lên, bạn có thể đấu điểm với 1 người trong tầm đánh của bạn, người thắng xem như sử dụng 1 [Sát] bỏ qua phòng cụ với người thua.

### Ai Vũ — `aiwu`

Một lần trong lượt của mỗi người, sau khi người khác nhận sát thương, bạn có thể bỏ từ 1 đến 3 lá, thực hiện lần lượt:
- Họ có thể bỏ từ 1 đến 3 lá;
- Nếu tổng số lá đã bỏ bởi kỹ năng này ≥ 3, bạn và họ hồi 1 máu.

### Quyết Biệt — `juebie`

Khi người khác có cùng thế lực với bạn trận vong, họ có thể giao tất cả bài của họ cho bạn.

### Chú Điển — `zhudian`

Sau khi bạn trở thành mục tiêu của lá Đen do người khác sử dụng, bạn có thể Trùng Chú 1 lá của bạn;
▷ Nếu lá bạn rút có màu Đen và khác chất với lá được sử dụng, bạn có thể mở lá đó và rút 1 lá.

### Bác Thông — `botong`

Bạn có thể chuyển hóa sử dụng 4 lá khác chất thành 1 lá cơ bản;
▶ Sau khi lá này kết toán xong, bạn có thể đem những lá này tùy ý giao cho những người khác.

### Định Loạn — `dingluan`

Một lần trong lượt của mỗi người, khi phán xét của 1 người ở khoảng cách ≤ số lá trên tay bạn có hiệu lực, nếu kết quả phán xét có chất BÍCH, bạn có thể chặn lần phán xét này;
▷ Bạn có thể xem như sử dụng 1 [Sát Hỏa] với họ.

### Thế Kích — `shiji`

Khi bạn gây sát thương thuộc tính cho người khác, nếu số lá trên tay bạn không phải nhiều nhất, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Bạn xem bài trên tay họ và bạn có thể bỏ tối đa 2 lá Đỏ trong đó;
- Bạn rút số lá tương đương với số lá đã bỏ.

### Dục Tước — `yujue`

Khi bắt đầu giai đoạn ra bài của người khác, nếu tổng số kỹ năng ghi trên những lá tướng đã mở của họ > bạn, bạn có thể bỏ 1 lá, yêu cầu họ chấp hành 1 [Quân Lệnh];
▶ Nếu họ chấp hành, sau khi họ gây sát thương trong lượt sau của họ, họ rút 2 lá;
▷ Nếu họ không chấp hành:
* Nếu họ đã mở tất cả tướng, bạn úp 1 tướng của họ và họ không thể mở tướng đó trong lượt này;
* Nếu họ có tướng úp, bạn lệnh họ thay đổi trạng thái chồng tướng.

## JiangeDefensePackage

Nguồn: `lang\vi_VN\Package\JiangeDefensePackage.lua`

Tên nhân vật nhận diện được: Liệt Đế Huyền Đức (`jg_liubei`); Thiên Hầu Khổng Minh (`jg_zhuge`); Công Thần Nguyệt Ánh (`jg_yueying`); Dục Hỏa Sĩ Nguyên (`jg_pangtong`); Vân Bình Thanh Long (`jg_qinglong_machine`); Cơ Lôi Bạch Hổ (`jg_baihu_machine`); Sỉ Vũ Chu Tước (`jg_zhuque_machine`); Linh Giáp Huyền Vũ (`jg_xuanwu_machine`); Giai Nhân Tử Đam (`jg_caozhen`); Tuyệt Trần Diệu Tài (`jg_xiahou`); Đoạn Ngục Trọng Đạt (`jg_sima`); Xảo Khôi Tuấn Nghệ (`jg_zhanghe`); Phước Địa Bệ Ngạn (`jg_bian_machine`); Thực hỏa Toan Nghê (`jg_suanni_machine`); Thôn Thiên Si Vẫn (`jg_chiwen_machine`); Liệt Thạch Nhai Xế (`jg_yazi_machine`); Dực Hán Vân Trường (`jg_guanyu`); Bồ Nguy Tử Long (`jg_zhaoyun`); Khô Mục Nguyên Nhượng (`jg_xiahoudun`); Bách Kế Văn Viễn (`jg_zhangliao`).

### Khích Trận — `jgjizhen`

Tỏa định kỹ: Khi bắt đầu giai đoạn kết thúc, bạn lệnh tất cả người Thục đã bị thương rút 1 lá.

### Linh Phong — `jglingfeng`

Khi bắt đầu giai đoạn rút bài, bạn có thể không rút bài, mở 2 lá trên đầu chồng bài rút rồi thu lấy; nếu 2 lá khác màu, lệnh 1 người Ngụy mất 1 máu.

### Thân Trận — `jgqinzhen`

Tỏa định kỹ: Khi người Thục bắt đầu giai đoạn ra bài, bạn lệnh giới hạn sử dụng [Sát] của họ +1 trong giai đoạn này.

### Biến Thiên — `jgbiantian`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể tiến hành phán xét, nếu kết quả phát xét có:
* Màu Đỏ: Cho đến khi bắt đầu lượt tiếp theo của bạn, khi người Ngụy tính toán sát thương Hỏa phải nhận, sát thương này +1;
* Chất BÍCH: Cho đến khi bắt đầu lượt tiếp theo của bạn, khi người Thục nhận sát thương Lôi, bạn chặn sát thương này.

### Công Thần — `jggongshen`

Khi bắt đầu giai đoạn kết thúc, bạn có thể chọn 1 mục:
1. Lệnh Khí Giới Thục hồi 1 máu; 2. Gây 1 sát thương Hỏa cho Khí Giới Ngụy.

### Trí Nang — `jgzhinang`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể mở 5 lá trên đầu chồng bài rút, sau đó bạn có thể giao tất cả lá phi cơ bản trong số đó cho 1 người Thục.

### Tinh Diệu — `jgjingmiao`

Tỏa định kỹ: Sau khi kết toán xong [Vô Giải Khả Kích] do người Ngụy sử dụng, lệnh họ mất 1 máu.

### jgyuhuo — `jgyuhuo`

Tỏa định kỹ: Khi bạn nhận sát thương Hỏa, chặn sát thương này.

### Thê Ngô — `jgqiwu`

Khi bạn sử dụng/đánh ra lá TÉP, có thể lệnh 1 người Thục hồi 1 máu.

### Thiên Ngục — `jgtianyu`

Khi bắt đầu giai đoạn kết thúc, bạn có thể đưa tất cả người Ngụy vào trạng thái xích.

### jgjiguan — `jgjiguan`

Tỏa định kỹ: Khi bạn trở thành mục tiêu của [Lạc Bất Tư Thục], hủy bỏ mục tiêu đối với bạn.

### Ma Tiễn — `jgmojian`

Tỏa định kỹ: Khi bắt đầu giai đoạn ra bài, bạn xem như sử dụng 1 [Vạn Tiễn Tề Phát] với tất cả người Ngụy.

### Trấn Vệ — `jgzhenwei`

Tỏa định kỹ: Khoảng cách từ người Ngụy đến người Thục +1

### Bôn Lôi — `jgbenlei`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể gây 2 sát thương Lôi cho Khí Giới Ngụy.

### Thiên Vẫn — `jgtianyun`

Khi bắt đầu giai đoạn kết thúc, bạn có thể mất 1 máu, chọn 1 người Ngụy, thực hiện lần lượt:
- Bạn gây 2 sát thương Hỏa cho họ;
- Bạn bỏ tất cả bài trong vùng trang bị của họ.

### Nghị Trọng — `jgyizhong`

Tỏa định kỹ: Nếu vùng trang bị của bạn không có phòng cụ, [Sát] Đen không có hiệu quả với bạn.

### Linh Dũ — `jglingyu`

Khi bắt đầu giai đoạn kết thúc, bạn có thể thay đổi trạng thái chồng tướng, sau đó lệnh tất cả người Thục khác đã bị thương hồi 1 máu.

### Trì Doanh — `jgchiying`

Tỏa định kỹ: Khi người Ngụy nhận sát thương, nếu sát thương này > 1, sát thương này trở thành 1.

### Kinh Phàm — `jgjingfan`

Tỏa định kỹ: Khoảng cách từ người Ngụy đến người Thục -1.

### Trấn Tây — `jgzhenxi`

Tỏa định kỹ: Sau khi người Ngụy nhận sát thương, tăng thêm 1 lá rút ở giai đoạn rút bài tiếp theo của bạn.

### Xuyên Vân — `jgchuanyun`

Khi bắt đầu giai đoạn kết thúc, bạn có thể gây 1 sát thương cho người khác có số máu ≥ bạn.

### Lôi Lệ — `jgleili`

Sau khi bạn gây sát thương do sử dụng [Sát], bạn có thể gây 1 sát thương Lôi cho 1 người Thục ngoài họ.

### Phong Hành — `jgfengxing`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể chọn 1 người Thục, xem như bạn sử dụng 1 [Sát] với họ.

### Khống Hồn — `jgkonghun`

Khi bắt đầu giai đoạn ra bài, nếu số máu đã mất của bạn ≥ số người thế lực Thục, bạn có thể gây 1 sát thương Lôi cho tất cả người Thục, sau đó bạn hồi X máu (X là số người đã nhận sát thương này).

### Phản Phệ — `jgfanshi`

Tỏa định kỹ: Khi bắt đầu giai đoạn kết thúc, bạn mất 1 máu.

### Huyền Lôi — `jgxuanlei`

Tỏa định kỹ: Khi bắt đầu giai đoạn chuẩn bị, bạn gây 1 sát thương Lôi cho tất cả người Thục có bài trong vùng phán xét.

### Hoặc Địch — `jghuodi`

Khi bắt đầu giai đoạn kết thúc, nếu có người Ngụy đang trong trạng thái chồng tướng, bạn có thể lệnh 1 người Thục thay đổi trạng thái chồng tướng.

### Tuyệt Cấp — `jgjueji`

Tỏa định kỹ: Giai đoạn rút bài của người Thục, nếu họ đã bị thương, lệnh họ rút ít đi 1 lá.

### Địa Động — `jgdidong`

Khi bắt đầu giai đoạn kết thúc, bạn có thể lệnh 1 người Thục thay đổi trạng thái chồng tướng.

### Luyện Ngục — `jglianyu`

Khi bắt đầu giai đoạn kết thúc, bạn có thể gây 1 sát thương Hỏa cho tất cả người Thục.

### Tham Thực — `jgtanshi`

Tỏa định kỹ: Khi bắt đầu giai đoạn kết thúc, bạn bỏ 1 lá trên tay.

### Thôn Phệ — `jgtunshi`

Tỏa định kỹ: Khi bắt đầu giai đoạn chuẩn bị, bạn gây 1 sát thương cho tất cả người Thục có số bài trên tay > của bạn.

### Nại Lạc — `jgnailuo`

Khi bắt đầu giai đoạn kết thúc, bạn có thể đặt chồng tướng;
▷ Bạn lệnh tất cả người Thục bỏ tất cả bài trong vùng trang bị của họ.

### Kiêu Nhuệ — `jgxiaorui`

Tỏa định kỹ: Khi người Thục gây sát thương bằng [Sát] trong giai đoạn ra bài của họ, bạn lệnh họ tăng 1 giới hạn sử dụng [Sát] trong giai đoạn này.

### Hổ Thần — `jghuchen`

Tỏa định kỹ:
• Khi bạn giết 1 người Ngụy, bạn nhận 1 [Hổ Thần].
• Giai đoạn rút bài, bạn rút +X lá (X là số [Hổ Thần]

### Thiên Tướng — `jgtianjiang`

Tỏa định kỹ: Khi người Thục gây sát thương bằng [Sát] lần đầu trong lượt này, bạn lệnh họ rút 1 lá.

### Phong Giam — `jgfengjian`

Tỏa định kỹ: Sau khi bạn gây sát thương cho người khác, bạn lệnh họ không thể sử dụng bài với bạn cho đến sau khi kết thúc lượt của họ.

### Khắc Định — `jgkeding`

Sau khi bạn chỉ định 1 mục tiêu duy nhất cho [Sát] hoặc công cụ phổ thông, bạn có thể bỏ ít nhất 1 lá trên tay và lệnh số người tương ứng với số lá bỏ cũng trở thành mục tiêu của lá này.

### Long Uy — `jglongwei`

Tỏa định kỹ: Khi người Thục trong trạng thái hấp hối, nếu giới hạn máu của bạn > 1, bạn có thể giảm 1 giới hạn máu, lệnh họ hồi đến 1 máu.

### Bạt Thi — `jgbashi`

Khi bạn trở thành mục tiêu của [Sát] hoặc công cụ phổ thông do người khác sử dụng, nếu bạn đang không trong trạng thái chồng tướng, bạn có thể thay đổi trạng thái chồng tướng, sau đó hủy bỏ mục tiêu đối với bạn.

### Đạm Tinh — `jgdanjing`

Khi người Ngụy tiến vào trạng thái hấp hối, nếu số máu của bạn > 1, bạn có thể mất 1 máu, bạn xem như sử dụng [Đào] với người hấp hối.

### Thống Quân — `jgtongjun`

Tỏa định kỹ: Tầm đánh của Khí Giới Ngụy +1

### Chước Giới — `jgjiaoxie`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 đến 2 Khí giới Thục có bài, lệnh họ giao cho bạn 1 lá.

### Soái Lệnh — `jgshuailing`

Tỏa định kỹ: Khi bắt đầu giai đoạn rút bài của người Ngụy, lệnh họ tiến hành phán xét, nếu kết quả có màu Đen, họ thu lấy kết quả phán xét.

## JoyPackage

Nguồn: `lang\vi_VN\Package\JoyPackage.lua`

### Thỉ — `shit`

Bài cơ bản

Thời điểm: Giai đoạn ra bài
Mục tiêu: Bạn
Hiệu quả: Không có

Hiệu ứng thêm: Trong lượt của bạn, khi lá này từ tay của bạn tiến vào chồng bài bỏ hoặc bàn chơi, nếu chất của lá này là:
* BÍCH: Mất 1 máu;
* TÉP: Bạn nhận 1 sát thương Lôi;
* RÔ: Bạn nhận 1 sát thương;
* CƠ: Bạn nhận 1 sát thương Hỏa.

### Hồng Thủy — `deluge`

Bài công cụ thời gian

Sử dụng: Trong giai đoạn ra bài.
Mục tiêu: Bạn.
Hiệu quả: Giai đoạn phán xét của mục tiêu, tiến hành phán xét, nếu kết quả phán xét có điểm là A hoặc K, mục tiêu ngẫu nhiên mở ra số bài bằng số người còn sống, theo vòng bắt đầu từ người tiếp theo với mục tiêu, mỗi người lần lượt nhận 1 lá từ số bài này, sau đó bỏ lá này
Nếu không, lá [Hồng Thủy] chuyển sang mục tiêu tiếp theo.

### Đài Phong — `typhoon`

Bài công cụ thời gian

Sử dụng: Trong giai đoạn ra bài.
Mục tiêu: Bạn.
Hiệu quả: Giai đoạn phán xét của mục tiêu, tiến hành phán xét, nếu kết quả phán xét từ 2~9 RÔ, những người có khoảng cách 1 với mục tiêu bỏ 6 lá trên tay, sau đó bỏ lá này. Nếu không, lá [Đài Phong] chuyển sang mục tiêu tiếp theo.

### Địa Chấn — `earthquake`

Bài công cụ thời gian

Sử dụng: Trong giai đoạn ra bài.
Mục tiêu: Bạn.
Hiệu quả: Giai đoạn phán xét của mục tiêu, tiến hành phán xét, nếu kết quả phán xét từ 2~9 TÉP, những người trong khoảng cách 1 với mục tiêu (bỏ qua hiệu ứng từ ngựa +1) bỏ tất cả trang bị, sau đó bỏ lá này. Nếu không, lá [Địa Chấn] chuyển sang mục tiêu tiếp theo.

### Hỏa Sơn — `volcano`

Bài công cụ thời gian

Sử dụng: Trong giai đoạn ra bài.
Mục tiêu: Bạn.
Hiệu quả: Giai đoạn phán xét của mục tiêu, tiến hành phán xét, nếu kết quả phán xét từ 2~9 CƠ, mục tiêu nhận 2 sát thương Hỏa, những người trong khoảng cách 1 với mục tiêu (bỏ qua hiệu ứng từ ngựa +1) nhận 1 sát thương Hỏa, sau đó bỏ lá này. Nếu không, lá [Hỏa Sơn] chuyển sang mục tiêu tiếp theo.

### Nễ Thạch Lưu — `mudslide`

Bài công cụ thời gian

Sử dụng: Trong giai đoạn ra bài.
Mục tiêu: Bạn.
Hiệu quả: Giai đoạn phán xét của mục tiêu, tiến hành phán xét, nếu kết quả phán xét có màu Đen và điểm là A, K, 4, 7, bắt đầu từ mục tiêu, bỏ nhiều bài từ vùng trang bị nhất có thể, người không có trang bị nhận 1 sát thương, hiệu quả dừng lại khi có 4 trang bị được bỏ đi, sau đó bỏ lá này
Nếu không, lá [Nễ Thạch Lưu] chuyển sang mục tiêu tiếp theo.

### Hầu Tử — `monkey`

Bài trang bị - Chiến Mã

Kỹ năng:
Khi người khác sử dụng [Đào], bạn có thể bỏ [Hầu Tử], loại bỏ mục tiêu của lá [Đào] này và thu lấy lá đó.
Tỏa định kỹ, khoảng cách từ bạn đến người khác -1.

### Dương Tu Kiếm — `yx_sword`

Bài trang bị - Vũ khí

Tầm đánh: 4
Kỹ năng: Khi lá [Sát] của bạn tạo gây thương, bạn có thể lệnh 1 người khác trong tầm đánh của bạn trở thành nguồn sát thương, sau đó bạn giao [Dương Tu Kiếm] cho họ.

## LangKhach

Nguồn: `lang\vi_VN\Package\LangKhach.lua`

Tên nhân vật nhận diện được: Vô Định (`wuding`); Triệu Thị Trinh (`zhaoshizhen`).

### Quân Lệnh Trạng — `military_order`

Bài công cụ

Mục tiêu: Bạn
Tác dụng:
• Bạn rút bài bằng số người của thế lực có nhiều người nhất ngoại trừ thế lực của bạn.
• Bạn chọn 1 lá bài/kỹ năng không có thời điểm và bị giới hạn số lần trong giai đoạn ra bài, trong giai đoạn này bạn được sử dụng/phát động thêm 1 lần đối với lá bài/kỹ năng đó.
• Sau khi bạn giết người trong giai đoạn này, bạn kết thúc giai đoạn ra bài, giới hạn trữ bài của bạn trở thành giới hạn máu.
• Sau khi kết thúc lượt này, nếu bạn không giết người sau khi lá này có hiệu quả, bạn trận vong.
• [Quân Lệnh Trạng] không có hiệu quả khi không sử dụng trực tiếp lá này.

### Biến Hóa — `bianhua`

Tỏa định kỹ:
• Sau khi mở tướng này lần đầu, bạn chọn 1 mục:
1. Bạn chọn 1 tướng đã mở trên bàn của người khác: Tướng này nhận giới tính, châu liên bích hợp và kỹ năng gốc ngoại trừ Quân chủ kỹ của tướng đã chọn;
2. Giới tính của tướng này là vô tính, bạn tăng 1 giới hạn máu, hồi 1 máu, nhận 1 tiêu ký [Dã tâm gia].
• Sau khi bắt đầu lượt, nếu tướng này đã mở và không có kỹ năng khác, bạn đổi phó tướng (Bỏ qua giới hạn đổi phó tướng).

### Bạch Tượng — `baixiang`

Tỏa định kỹ:
• [Nam Man Nhập Xâm] không có hiệu quả với bạn.
• Nếu bạn không có Ngựa trong vùng trang bị, khoảng cách từ người khác đến bạn +1, tầm đánh của bạn +1.

### Bà Vương — `powang`

Chủ tướng kỹ, Giảm 0.5 máu gốc: Một lần trong giai đoạn ra bài, bạn có thể chuyển hóa sử dụng 1 lá có điểm A/Q/K thành [Nam Man Nhập Xâm] với tất cả người khác thuộc 1 thế lực;
▶ Khi bạn gây sát thương bởi [Nam Man Nhập Xâm] này, nếu mục tiêu có lá trong vùng trang bị, bạn có thể chặn sát thương này, sau đó bạn bỏ tất cả lá trong vùng trang bị của mục tiêu.

### Sinh Vi Tướng — `shengweijiang`

Sau khi bạn giải quyết hấp hối, nếu số máu của bạn ≤0, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Bạn hồi máu đến tối đa và bổ xung bài trên tay tới giới hạn máu;
- Lệnh người đang trong giai đoạn ra bài kết thúc giai đoạn này;
- Bạn mất kỹ năng này, nhận kỹ năng »Tử Vi Thần«.

### Tử Vi Thần — `siweishen`

• Một lần trong ván đấu, khi người cùng thế lực với bạn gây sát thương, bạn có thể lệnh sát thương này +1.
• Tỏa định kỹ: Sau khi bạn kết thúc lượt, bạn trận vong.

## LordEXPackage

Nguồn: `lang\vi_VN\Package\LordEXPackage.lua`

Tên nhân vật nhận diện được: Mạnh Đạt (`mengda`); Đường Tư (`tangzi`); Trương Lỗ (`zhanglu`); Mi Phương & Phó Sĩ Nhân (`mifangfushiren`); Lưu Kỳ (`liuqi`); Sĩ Nhiếp (`shixie`); Chung Hội (`zhonghui`); Đổng Chiêu (`dongzhao`); Từ Thứ (`xushu`); Ngô Cảnh (`wujing`); Nghiêm Bạch Hổ (`yanbaihu`); Tư Mã Chiêu (`simazhao`); Hứa Du (`xuyou`); Hạ Hầu Bá (`xiahouba`); Gia Cát Khác (`zhugeke`); Ngạo Tài (`aocai`); Tôn Lâm (`sunchen`); Phan Tuấn (`panjun`); Văn Khâm (`wenqin`); Hoàng Tổ (`huangzu`); Công Tôn Uyên (`gongsunyuan`); Bành Dạng (`pengyang`); Tô Phi (`sufei`); Lưu Ba (`liuba`); Chu Linh (`zhuling`).

### Cầu An — `qiuan`

Khi bạn nhận sát thương, nếu bạn không có [Hàm], bạn có thể đem lá gây sát thương cho bạn đặt lên tướng này, gọi là [Hàm], sau đó chặn sát thương này.

### Lượng Phản — `liangfan`

Tỏa định kỹ: Khi bắt đầu giai đoạn chuẩn bị, nếu bạn có [Hàm], bạn mất 1 máu, sau đó thu lấy tất cả [Hàm];
▶ Trong lượt này, sau khi bạn gây sát thương cho 1 người do sử dụng [Hàm], bạn có thể thu lấy 1 lá của họ.

### Hưng Thạo — `xingzhao`

Tỏa định kỹ: Dựa theo số thế lực trên bàn chơi có người bị thương:
* 1+: Bạn có kỹ năng »Tuân Tuân«.
* 2+: Sau khi bạn nhận sát thương, nếu số bài trên tay bạn và nguồn sát thương khác nhau, người ít bài trên tay hơn rút 1 lá.
* 3+: Khi bắt đầu giai đoạn bỏ bài, giới hạn trữ bài của bạn +4.
* 4+: Khi bạn mất bài trong vùng trang bị, bạn rút 1 lá.

### Bố Thí — `bushi`

• Khi kết thúc lượt, bạn nhận X [Nghĩa Xá] (X là số máu của bạn).
• Khi bắt đầu giai đoạn chuẩn bị của người khác, nếu bạn có [Nghĩa Xá], bạn có thể giao 1 lá cho họ, sau đó bạn bỏ 1 [Nghĩa Xá] và rút 2 lá.
• Khi bắt đầu giai đoạn chuẩn bị, bạn bỏ X lá (X là số người còn sống trừ số máu của bạn và trừ 2), sau đó bỏ tất cả [Nghĩa Xá].

### Mễ Đạo — `midao`

• Khi bắt đầu giai đoạn kết thúc, nếu không có [Mễ], bạn có thể rút 2 lá, sau đó bạn đặt 2 lá lên tướng này, gọi là [Mễ].
• Khi phán xét của 1 người có hiệu lực, bạn có thể đánh ra 1 [Mễ] để thay đổi kết quả phán xét, sau đó thu lấy lá phán xét ban đầu.

### Phong Thế — `fengshix`

• Sau khi bài bạn sử dụng xác định 1 mục tiêu duy nhất, nếu số bài trên tay họ < bạn, bạn có thể bỏ 1 lá của bạn và họ, lệnh sát thương từ lá này +1.
• Sau khi bạn trở thành mục tiêu duy nhất của bài do người khác sử dụng, nếu số lá trên tay bạn < họ, họ có thể lệnh bạn bỏ 1 lá của bạn và họ, lệnh sát thương từ lá này +1.

### Vấn Kế — `wenji`

Khi bắt đầu giai đoạn ra bài, bạn có thể lệnh 1 người khác giao cho bạn 1 lá ngửa mặt:
* Nếu họ cùng thế lực với bạn hoặc không có thế lực, lượt này bạn sử dụng lá này không giới hạn khoảng cách và số lần và không thể hưởng ứng;
* Nếu họ thế lực xác định khác bạn, bạn giao cho họ 1 lá bài khác ngửa mặt.

### Truân Giang — `tunjiang`

Khi bắt đầu giai đoạn kết thúc, nếu bạn trong giai đoạn ra bài đã sử dụng ít nhất 1 lá và không chỉ định người khác làm mục tiêu, bạn có thể rút X lá (X là số thế lực trên bàn chơi).

### Tị Loạn — `biluan`

Tỏa định kỹ: Khoảng cách từ người khác tới bạn +X (X là số lá trong vùng trang bị của bạn).

### Lễ Hạ — `lixia`

Tỏa định kỹ: Khi bắt đầu giai đoạn chuẩn bị của người thế lực khác bạn, nếu bạn không ở trong tầm đánh của họ, bạn lệnh họ chọn 1 mục:
1. Lệnh bạn rút 1 lá;
2. Bỏ 1 lá trong vùng trang bị của bạn, sau đó họ mất 1 máu.

### Quyền Kế — `quanji`

• Một lần trong lượt của mỗi người ứng với mỗi thời điểm, sau khi bạn gây hoặc nhận sát thương, bạn có thể rút 1 lá, sau đó đặt ngửa 1 lá lên tướng này, gọi là [Quyền].
• Giới hạn trữ bài của bạn +X (X là số [Quyền]).

### Bài Dị — `paiyi`

Một lần trong giai đoạn ra bài, bạn có thể đưa 1 [Quyền] vào chồng bài bỏ và chọn 1 người, họ rút X lá (X là số [Quyền] bạn có, tối đa 7);
▷ Nếu số bài trên tay họ > bạn, bạn gây 1 sát thương cho họ.

### Khuyến Tiến — `quanjin`

Một lần trong giai đoạn ra bài, bạn có thể giao 1 lá trên tay cho người từng nhận sát thương trong giai đoạn này và lệnh họ chấp hành 1 [Quân Lệnh]:
* Nếu họ chấp hành, bạn rút 1 lá;
* Nếu họ không chấp hành và bạn không phải người có nhiều bài trên tay nhất, bạn bổ sung bài trên tay đến khi bằng người có nhiều bài trên tay nhất, tối đa 5 lá.

### Tạc Vận — `zaoyun`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người thế lực xác định với bạn và khoảng cách từ bạn đến họ lớn hơn 1 và bỏ X lá bài trên tay (X là khoảng cách từ bạn đến họ -1), lệnh khoảng cách từ bạn đến họ là 1 trong lượt này, sau đó bạn gây 1 sát thương cho họ.

### Khiêm Sách — `qiance`

Sau khi người cùng thế lực với bạn xác định mục tiêu của lá công cụ, họ có thể lệnh những mục tiêu thuộc Đại thế lực không thể hướng ứng với lá này.

### Cử Tiến — `jujian`

Phó tướng kỹ, Giảm 0.5 máu gốc: Khi 1 người cùng thế lực với bạn tiến vào trạng thái hấp hối, bạn có thể lệnh họ hồi đến 1 máu, sau đó bạn đổi Phó tướng.

### Điều Quy — `diaogui`

Một lần trong giai đoạn ra bài, có thể sử dụng 1 lá trang bị như [Điệu Hổ Ly Sơn];
▷ Nếu thế lực của bạn có sự thay đổi về đội hình do phát động kỹ năng này, bạn rút X lá (X là số người của đội hình đông nhất trong những quan hệ đội hình ở thế lực của bạn có sự thay đổi).

### Phong Dương — `fengyang`

Trận pháp kỹ: Quan hệ đội hình: Người thế lực xác định khác bạn không thể thu lấy hoặc bỏ trang bị của người cùng đội hình với bạn.

### Trĩ Đạo — `zhidao`

Tỏa định kỹ: Khi bắt đầu giai đoạn ra bài, bạn chọn 1 người khác, trong lượt này:
* Khoảng cách từ bạn đến họ là 1;
* Bạn không thể chỉ định người khác ngoại trừ họ làm mục tiêu sử dụng bài;
▶ Sau khi bạn gây sát thương cho họ lần đầu tiên trong giai đoạn này, bạn thu lấy 1 lá trong vùng chơi của họ.

### Ký Li — `jilix`

Tỏa định kỹ:
• Sau khi kết toán xong lá cơ bản Đỏ hoặc công cụ phổ thông Đỏ, nếu bạn là mục tiêu duy nhất của lá này, bạn lệnh cho người sử dụng xem như sử dụng lá cùng tên với lá đó với bạn (không giới hạn khoảng cách, số lần sử dụng);
• Khi bạn nhận sát thương lần thứ 2 trong cùng 1 giai đoạn, bạn chặn sát thương và loại bỏ tướng này.

### Chiếu Thư — `ImperialEdict`

Bài Trang bị - Bảo vật

Kỹ năng:
• Sau khi sử dụng lá này, bạn đặt lá này vào vùng tướng của bạn.

• Một lần trong giai đoạn ra bài của người có cùng thế lực với bạn, nếu họ thuộc tiểu thế lực, có thể đặt tối đa 2 lá trên tay lên tướng của bạn; nếu không thuộc tiểu thế lực, họ có thể đặt 1 lá trên tay lên tướng của bạn, gọi là [Chiếu].
• Một lần trong giai đoạn ra bài, nếu có 4 [Chiếu] không cùng chất, bạn có thể đưa tất cả [Chiếu] vào chồng bài bỏ, rút ngẫu nhiêu 1 lá công cụ thế lực.


### Đặt bài trên tay — `imperialedictattach`

Một lần trong giai đoạn ra bài của người có cùng thế lực với bạn, nếu họ thuộc tiểu thế lực, có thể đặt tối đa 2 lá trên tay lên tướng của bạn; nếu không thuộc tiểu thế lực, họ có thể đặt 1 lá trên tay lên tướng của bạn, gọi là [Chiếu].

### Nhận bài công cụ — `imperialedicttrick`

Một lần trong giai đoạn ra bài, nếu có 4 lá [Chiếu] không cùng chất, bạn có thể đưa tất cả [Chiếu] vào chồng bài bỏ, rút ngẫu nhiêu 1 lá công cụ thế lực.

### Hiệu Lệnh Thiên Hạ — `rule_the_world`

Bài công cụ - Ngụy

Mục tiêu: Một người không phải ít máu nhất
Hiệu quả: Ngoại trừ mục tiêu, mỗi người có thể lựa chọn 1 mục:
1. Bỏ 1 lá trên tay và xem như sử dụng [Sát] không giới hạn khoảng cách với mục tiêu (Người thế lực Ngụy không cần bỏ bài);
2. Bỏ 1 lá của mục tiêu (Người thế lực Ngụy thu lấy lá đó thay vì bỏ).

### Khắc Phục Trung Nguyên — `conquering`

Bài công cụ - Thục

Mục tiêu: Tùy ý
Hiệu quả: Mục tiêu lựa chọn 1 mục:
1. Xem như sử dụng [Sát] (Sát thương từ [Sát] này +1 nếu do người thế lực Thục sử dụng);
Rút 1 lá (Người thế lực Thục đổi thành rút 2 lá).

### Cố Quốc An Bang — `consolidate_country`

Bài công cụ - Ngô

Mục tiêu: Bạn
Hiệu quả: Mục tiêu rút 8 lá sau đó bỏ ít nhất 6 lá trên tay, nếu bạn thuộc thế lực Ngô, có thể giao tùy ý tối đa 6 lá trong số những lá bỏ cho những người khác thuộc thế lực Ngô, mỗi người tối đa 2 lá.

### Văn Hòa Loạn Võ — `chaos`

Bài công cụ - Quần

Mục tiêu: Tất cả
Hiệu quả: Mục tiêu mở bài trên tay, sau đó bạn chọn 1 mục:
1. Lệnh họ bỏ 2 lá khác loại trên tay;
2. Bỏ 1 lá trên tay họ;
Người thế lực Quần sau khi chấp hành lựa chọn của bạn, nếu họ không có bài trên tay, họ bổ sung bài trên tay tới máu hiện tại.

### Túc Trí — `suzhi`

Tỏa định kỹ:
• Giới hạn ba lần trong lượt của bạn đối với các mục sau:
* Khi bạn gây sát thương cho mục tiêu của [Sát] hoặc [Quyết Đấu], bạn lệnh số sát thương +1;
* Khi bạn sử dụng công cụ phi chuyển hóa, bạn rút 1 lá;
* Sau khi bài của người khác tiến vào chồng bài bỏ do bỏ đi, bạn thu lấy 1 lá của họ.
• Nếu chưa phát động »Túc Trí« 3 lần trong lượt:
* Bạn có thể sử dụng công cụ phi chuyển hóa không giới hạn khoảng cách;
* Khi bạn kết thúc lượt, bạn nhận kỹ năng »Phản Quỹ« đến khi bắt đầu lượt tiếp theo của bạn.

### Chiêu Tâm — `zhaoxin`

Sau khi bạn nhận sát thương, bạn có thể mở tất cả bài trên tay, sau đó hoán đổi bài trên tay với 1 người khác có số lá trên tay ≤ bạn.

### Thành Lược — `chenglve`

Sau khi kết toán bài do 1 người cùng thế lực với bạn sử dụng, nếu số mục tiêu > 1, bạn có thể lệnh họ rút 1 lá;
▷ Nếu bạn đã nhận sát thương từ lá này, bạn có thể lệnh 1 người cùng thế lực với bạn không có tướng úp và không có tiêu ký nào nhận được 1 tiêu ký [Âm Dương Ngư].

### Thị Tài — `shicai`

Tỏa định kỹ: Sau khi bạn nhận sát thương, nếu số sát thương là:
* 1: Bạn rút 1 lá;
* 2+: Bạn bỏ 2 lá.

### Báo Liệt — `baolie`

Tỏa định kỹ:
• Khi bắt đầu giai đoạn ra bài, lệnh những người thế lực xác định khác bạn có tầm đánh đến bạn sử dụng [Sát] với bạn, nếu không, bạn bỏ 1 lá của họ.
• Bạn sử dụng [Sát] với người có máu ≥ bạn không giới hạn khoảng cách và số lần.

### Ngạo Tài — `aocai`

Ngoài lượt của bạn, khi bạn cần sử dụng/đánh ra bài cơ bản, bạn có thể xem hai lá trên đầu chồng bài, bạn có thể sử dụng/đánh ra lá cơ bản có tên tương ứng trong đó.

### Độc Võ — `duwu`

Hạn định kỹ: Giai đoạn ra bài, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Bạn chọn 1 [Quân Lệnh], yêu cầu tất cả người thế lực khác bạn chấp hành [Quân Lệnh] này; nếu họ không chấp hành, bạn gây 1 sát thương cho họ và rút một lá;
- Nếu trong những người còn sống có người đã tiến vào trạng thái hấp hối trong quá trình trên, bạn mất 1 máu.

### Thị Lực — `shilu`

• Sau khi có người trận vong, nếu họ có tướng, bạn có thể đặt tất cả tướng của họ lên tướng này, gọi là [Lục];
▷ Nếu họ bị bạn giết, bạn nhận 2 lá từ chồng bài tướng đặt lên tướng này, gọi là [Lục].
• Khi bắt đầu giai đoạn chuẩn bị, nếu bạn có [Lục], bạn có thể bỏ tối đa X lá (X là số [Lục]), sau đó rút số lá tương ứng.

### Hung Ngược — `xiongnve`

• Khi bắt đầu giai đoạn ra bài, bạn có thể bỏ 1 [Lục], chọn 1 mục có hiệu quả trong lượt này:
1. Khi bạn gây sát thương cho người cùng thế lực với [Lục] đã bỏ, sát thương này +1;
2. Khi bạn gây sát thương cho người cùng thế lực với [Lục] đã bỏ, thu lấy 1 lá của họ;
3. Bạn sử dụng bài với mục tiêu cùng thế lực với [Lục] đã bỏ không giới hạn số lần.
• Khi kết thúc giai đoạn ra bài, bạn có thể bỏ 2 [Lục], đến khi bắt đầu lượt tiếp theo của bạn, khi bạn tính toán sát thương phải nhận từ người khác, sát thương này -1. 

### Quan Vy — `congcha`

• Khi bắt đầu giai đoạn chuẩn bị, bạn có thể chọn 1 người không có thế lực;
▶ Cho đến khi bắt đầu lượt tiếp theo của bạn, khi họ mở tướng và trở thành có thế lực, nếu của họ và bạn:
* Cùng thế lực: Bạn và họ rút 2 lá;
* Khác thế lực: Họ mất 1 máu.
• Giai đoạn rút bài, nếu không có người không có thế lực, bạn có thể lệnh số lá rút +2.

### Công Thanh — `gongqing`

Tỏa định kỹ:
• Khi bạn tính toán sát thương phải nhận, nếu tầm đánh của nguồn sát thương lớn hơn 3, sát thương này +1;
• Khi bạn nhận sát thương, nếu tầm đánh của nguồn sát thương nhỏ hơn 3 và sát thương lớn hơn 1, sát thương này trở thành 1.

### Căng Phạt — `jinfa`

Một lần trong giai đoạn ra bài, có thể bỏ 1 lá và chọn 1 người khác có bài, họ chọn 1 mục:
1. Lệnh bạn lấy 1 lá của họ;
2. Họ giao 1 lá trang bị cho bạn, nếu bạn nhận được lá ♠ và lá đó còn trên tay bạn, xem như họ sử dụng 1 [Sát] với bạn.

### Vãn Cung — `xishe`

• Khi bắt đầu giai đoạn chuẩn bị của người khác, bạn có thể bỏ 1 lá trong vùng trang bị và xem như sử dụng 1 [Sát] với họ, nếu số máu của họ nhỏ hơn của bạn, bạn lệnh cho [Sát] này không thể hưởng ứng; bạn có thể lặp lại quá trình này.
• Khi kết thúc lượt này, nếu trong lượt người trận vong và nguồn là [Sát] từ kỹ năng này của bạn, bạn có thể đổi phó tướng, tướng sau khi đổi được úp xuống.

### Hoài Dị — `huaiyi`

• Một lần trong giai đoạn ra bài, bạn có thể mở toàn bộ bài trên tay, nếu có đủ 2 màu, bạn thực hiện lần lượt:
- Bạn chọn 1 màu và bỏ những lá trên tay có màu này;
- Bạn chọn tối đa X người có bài, thu lấy 1 lá của họ (X là số lá bạn vừa bỏ), nếu lá được thu lấy là trang bị thì đặt lá đó lên tướng này thay vì thu lấy, gọi là [Dị].
• Bạn có thể sử dụng hoặc đánh ra [Dị] như bài trên tay.

### Tứ Tuy — `zisui`

Tỏa định kỹ:
• Giai đoạn rút bài, nếu có [Dị], bạn rút thêm X lá (X là số [Dị]).
• Khi bắt đầu giai đoạn kết thúc, nếu số [Dị] > giới hạn máu của bạn, bạn trận vong.

### Thông Linh — `tongling`

Một lần trong giai đoạn ra bài, sau khi bạn gây sát thương cho 1 người thế lực xác định khác bạn (A), bạn có thể chọn 1 người cùng thế lực với bạn (B), B có thể sử dụng 1 lá có bao gồm A là mục tiêu;
* Nếu lá này gấy sát thương, bạn và B rút 2 lá;
* Nếu lá này không gây sát thương, bạn lệnh A thu lấy lá bạn đã sử dụng để gây sát thương cho A.

### Cận Hãm — `jinxian`

Sau khi bạn mở tướng này, bạn lệnh tất cả người ở khoảng cách ≤1 thực hiện: Nếu họ đã:
* Mở tất cả tướng: Họ úp 1 tướng
* Có tướng úp: Họ bỏ 2 lá.

### Liên Phiên — `lianpian`

Khi bắt đầu giai đoạn kết thúc của 1 người, nếu trong lượt này tổng số lá tiến vào chồng bài bỏ do bạn chỉ định bỏ đi > số máu của bạn, nếu lượt này là lượt của:
* Bạn: Bạn có thể lệnh 1 người cùng thế lực với bạn bổ sung bài trên tay đến giới hạn máu của họ;
* Người khác: Họ có thể chọn bỏ 1 lá của bạn hoặc lệnh bạn hồi 1 máu.

### Trù Độ — `tongdu`

Khi bắt đầu giai đoạn kết thúc của người cùng thế lực với bạn, họ có thể rút X lá (X là số bài họ đã bỏ trong giai đoạn bỏ bài ở lượt này, tối đa 3).

### Quy Ẩn — `qingyin`

Hạn định kỹ: Giai đoạn ra bài, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Lệnh tất cả người cùng thế lực với bạn hồi đầy máu;
- Bạn loại bỏ tướng này.

### Trấn Vệ — `juejue`

• Khi bắt đầu giai đoạn bỏ bài, bạn có thể mất 1 máu; Nếu làm vậy, khi kết thúc giai đoạn này, nếu trong giai đoạn này bạn có bỏ bài, bạn lệnh tất cả người khác chọn 1 mục:
1. Họ đưa X lá trên tay vào chồng bài bỏ (X là số lá bạn đã bỏ trong giai đoạn này);
2. Bạn gây 1 sát thương cho họ.
• Khi bạn giết người cùng thế lực với bạn, bạn bỏ qua chấp hành thưởng phạt.

### Ngư Lân — `fangyuan`

Trận pháp kỹ: Quan hệ vây công:
• Nếu bạn là người vây công, giới hạn trữ bài của người vây công +1, giới hạn trữ bài của người bị vây công -1.
• Khi bắt đầu giai đoạn kết thúc, nếu bạn là người bị vây công trong quan hệ vây công, bạn xem như sử dụng [Sát] với 1 người vây công

## ManoeuvrePackage

Nguồn: `lang\vi_VN\Package\ManoeuvrePackage.lua`

Tên nhân vật nhận diện được: Hoa Hâm (`huaxin`); Lục Úc Sinh (`luyusheng`); Tông Dự (`zongyux`); Nễ Hành (`miheng`); Phùng Hy (`fengxi`); Đặng Chi (`dengzhi`); Tuân Kham (`xunchen`); Dương Hỗ (`yanghu`).

### Vong Quy — `wanggui`

Một lần trong lượt của mỗi người, sau khi bạn gây hoặc nhận sát thương và bạn đã mở tướng này, nếu tướng còn lại của bạn:
* Chưa mở: Bạn có thể gây 1 sát thương cho người thế lực xác định khác bạn;
* Đã mở: Bạn có thể lệnh những người cùng thế lực rút 1 lá.

### Tức Binh — `xibing`

Sau khi 1 người khác lần đầu trong giai đoạn ra bài của họ xác định 1 mục tiêu duy nhất của lá [Sát] Đen hoặc công cụ phổ thông Đen, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Nếu số lá trên tay họ < số máu của họ, bạn lệnh họ bổ sung bài trên tay đến số máu của họ và không thể tiếp tục sử dụng bài trên tay trong lượt này;
- Nếu bạn và họ đã mở tất cả tướng, bạn có thể úp 1 tướng của bạn và họ, trong lượt này không thể mở lại tướng đó.

### Trinh Đặc — `zhente`

Một lần trong lượt của mỗi người, sau khi trở thành mục tiêu của lá cơ bản Đen hoặc công cụ phổ thông Đen do người khác sử dụng, có thể lệnh cho họ chọn 1 mục:
1. Lượt này họ không thể sử dụng bài Đen;
2. Lá này không có hiệu quả với bạn.

### Chi Vi — `zhiwei`

Sau khi bạn mở tướng này, bạn có thể chọn 1 người khác, đến khi tướng này bị úp hoặc loại bỏ:
▶ Sau khi họ gây sát thương, bạn rút 1 lá;
▶ Sau khi họ nhận sát thương, bạn bỏ 1 lá ngẫu nhiên trên tay;
▶ Khi kết thúc giai đoạn bỏ bài, bạn lệnh họ thu lấy tất cả bài bỏ trong giai đoạn này của bạn;
▶ Khi họ trận vong, nếu bạn đã mở tất cả tướng, bạn úp tướng này.

### Khí Ngạo — `qiao`

Hai lần trong giai đoạn ra bài của mỗi người, sau khi bạn trở thành mục tiêu của bài do người thế lực khác bạn sử dụng, bạn có thể bỏ 1 lá của họ, sau đó bạn bỏ 1 lá.

### Thừa Thưởng — `chengshang`

Một lần trong giai đoạn ra bài, sau khi bài do bạn sử dụng kết toán xong, nếu lá này thỏa mãn những điều sau:
* Số lá được đem sử dụng là 1;
* Lá này có chỉ định người thế lực khác làm mục tiêu;
* Lá này không gây sát thương;
▷ Bạn có thể thu lấy những lá có cùng chất và điểm với lá đó trong chồng bài rút;
▷ Nếu bạn không thu được bài sau khi phát động kỹ năng này, bạn thêm 1 lần phát động kỹ năng này trong giai đoạn này.

### Cuồng Tài — `kuangcai`

Tỏa định kỹ:
• Bài bạn sử dụng trong lượt không bị giới hạn khoảng cách và số lần sử dụng;
• Khi bắt đầu giai đoạn bỏ bài, nếu trong lượt này:
* Bạn có sử dụng bài và không gây sát thương: Giới hạn trữ bài của bạn trở về sau -1;
* Bạn không sử dụng bài: Giới hạn trữ bài của bạn trở về sau +1.

### Thiệt Kiếm — `shejian`

Sau khi bạn trở thành mục tiêu duy nhất của bài do người khác sử dụng, nếu không có ai đang giải quyết hấp hối, bạn có thể bỏ tất cả bài trên tay (tối thiếu 1), sau đó chọn 1 mục:
1. Bạn bỏ X lá của người sử dụng bài (X là số lá bạn đã bỏ);
2. Bạn gây 1 sát thương cho người sử dụng bài.

### Ngọc Toái — `yusui`

Một lần trong lượt của mỗi người, sau khi bạn trở thành mục tiêu của bài Đen do người thế lực xác định khác bạn sử dụng, bạn có thể mất 1 máu, sau đó lựa chọn 1 mục:
1. Bạn lệnh họ bỏ X lá trên tay (X là giới hạn máu của họ);
2. Bạn lệnh họ mất máu đến khi bằng với số máu của bạn.

### Bác Ngôn — `boyan`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người khác, thực hiện lần lượt:
- Họ bổ sung bài trên tay đến giới hạn máu của họ;
- Trong lượt này họ không thể sử dụng hoặc đánh ra bài trên tay của họ;
▷ Tung Hoành: Bạn có thể lệnh họ nhận kỹ năng »Bác Ngôn (Tung Hoành)« (Bỏ qua dòng đầu và hiệu ứng Tung Hoành) cho đến sau khi kết thúc lượt chơi tiếp theo của họ.

### Bác Ngôn — `boyanzongheng`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người khác, lệnh họ trong lượt này không thể sử dụng hoặc đánh ra bài trên tay của họ.

### Giản Lượng — `jianliang`

Đầu giai đoạn rút bài, nếu bạn là người có ít bài trên tay nhất, bạn có thể lệnh người cùng thế lực bạn lần lượt rút 1 lá.

### Ngụy Minh — `weimeng`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người khác có bài trên tay, bạn thu lấy tối đa X lá trên tay của họ (X là số máu của bạn), sau đó bạn giao lượng bài tương đương cho họ;
▷ Tung Hoành: Bạn có thể lệnh họ nhận kỹ năng »Ngụy Minh (Tung Hoành)« (Thay mô tả "X" thành "1" và bỏ qua hiệu ứng Tung Hoành) cho đến sau khi kết thúc lượt tiếp theo của họ.

### Ngụy Minh — `weimengzongheng`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người khác có bài trên tay, bạn thu lấy 1 lá trên tay của họ, sau đó giao 1 lá cho họ.

### Phong Lược — `fenglve`

Một lần trong giai đoạn ra bài, bạn có thể đấu điểm với 1 người khác:
* Nếu bạn thắng, họ giao 2 lá trong vùng chơi của họ cho bạn;
* Nếu bạn thua, bạn giao 1 lá cho họ;
▷ Tung Hoành: Bạn có thể lệnh họ nhận kỹ năng »Phong Lược (Tung Hoành)« (Thay mô tả "2" thành "1" và bỏ qua hiệu ứng Tung Hoành) cho đến sau khi kết thúc lượt tiếp theo của họ.

### Ám Dũng — `anyong`

Một lần trong lượt của mỗi người, khi 1 người cùng thế lực với bạn gây sát thương cho 1 người khác ngoài họ, có thể lệnh cho sát thương này gấp đôi; sau đó, nếu người nhận sát thương đã:
* Mở tất cả tướng: Bạn tự mất 1 máu và mất kỹ năng này;
* Mở 1 tướng và không phải tất cả: Bạn bỏ 2 lá trên tay.

### Phong Lược — `fenglvezongheng`

Một lần trong giai đoạn ra bài, bạn có thể đấu điểm với 1 người khác. Nếu thắng, họ giao 1 lá trong vùng chơi của họ cho bạn; nếu thua, bạn giao 1 lá cho họ.

### Đức Thiệu — `deshao`

X lần trong lượt của mỗi người (X là số máu của bạn), sau khi bạn trở thành mục tiêu duy nhất của bài Đen do người khác sử dụng, nếu họ đã mở số tướng ≤ hơn bạn, bạn có thể bỏ 1 lá của họ.

### Minh Phạt — `mingfa`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người khác thế lực;
▶ Khi kết thúc lượt tiếp theo của họ, nếu số lá trên tay họ so với bạn:
* Ít hơn: Bạn gây 1 sát thương cho họ và thu lấy 1 lá trên tay họ;
* Nhiều hơn: Bạn bổ sung bài trên tay đến khi bằng họ, tối đa rút thêm 5 lá.

## MOLPackage

Nguồn: `lang\vi_VN\Package\MOLPackage.lua`

Tên nhân vật nhận diện được: Đỗ Dự (`duyu`); Lý Phong (`lifeng`); Lăng Tháo (`lingcao`).

### Vũ Khố — `wuku`

Tỏa định kỹ: Khi 1 người thế lực xác định khác bạn sử dụng 1 trang bị, bạn tăng 1 [Võ Khố] (Tối đa 2).

### Diệt Ngô — `miewu`

Một lần trong lượt của mỗi người, khi bạn cần sử dụng/đánh ra 1 lá cơ bản/công cụ, bạn có thể giảm 1 [Võ Khố] để chuyển hóa sử dụng/đánh ra 1 lá thành 1 lá cơ bản/công cụ đó, sau đó bạn rút 1 lá.

### Truân Trữ — `tunchu`

Giai đoạn rút bài, bạn có thể rút thêm 2 lá;
▷ Bạn không thể sử dụng [Sát] trong lượt này;
▶ Khi kết thúc giai đoạn rút bài, bạn đặt từ 1 đến 2 lá trên tay lên tướng này, gọi là [Lương].

### Thâu Lương — `shuliang`

Khi bắt đầu giai đoạn kết thúc của 1 người cùng thế lực với bạn, nếu khoảng cách từ bạn đến họ ≤ số [Lương], bạn có thể đưa 1 [Lương] vào chồng bài bỏ, lệnh họ rút 2 lá.

### Độc Tiến — `dujin`

• Sau khi bạn mở tướng này lần đầu, nếu không có người nào khác có cùng thế lực với bạn (bao gồm cả người đã trận vong), bạn nhận 1 tiêu ký [Tiên Khu].
• Giai đoạn rút bài, bạn có thể rút thêm X lá (X là 1 nửa số lá trong vùng trang bị của bạn, làm tròn lên).

## MomentumPackage

Nguồn: `lang\vi_VN\Package\MomentumPackage.lua`

Tên nhân vật nhận diện được: Lý Điển (`lidian`); Tang Bá (`zangba`); Mã Đại (`madai`); My Phu Nhân (`mifuren`); Tôn Sách (`sunce`); Anh Hồn (`yinghun_sunce`); Trấn Vũ & Đổng Tập (`chenwudongxi`); Đổng Trác (`dongzhuo`); Trương Nhiệm (`zhangren`); Trương Giác - Quân (`lord_zhangjiao`).

### Tuân Tuân — `xunxun`

Khi bắt đầu giai đoạn rút bài, bạn có thể xem 4 lá trên đầu chồng bài rút, sau đó đặt 2 lá trong số đó lên đầu chồng bài rút, còn lại đặt xuống đáy chồng bài rút.

### Vong Khích — `wangxi`

Sau khi bạn gây/nhận sát thương cho/từ người khác, ứng với mỗi sát thương, bạn có thể lệnh bạn và họ rút 1 lá.

### Hoành Giang — `hengjiang`

Sau khi bạn nhận sát thương, ứng với mỗi sát thương, nếu giới hạn trữ bài của người đang có lượt > 0, bạn có thể lệnh người đang có lượt giảm 1 giới hạn trữ bài;
▶ Khi kết thúc lượt này, nếu ở giai đoạn bỏ bài, họ không bỏ lá nào, bạn rút X lá bài (X là số lần bạn đã phát động kỹ năng này trong lượt này).

### Tiềm Tập — `qianxi`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể rút 1 lá, sau đó bỏ 1 lá và chọn 1 người khác ở khoảng cách 1;
▶ Trong lượt này, họ không thể sử dụng/đánh ra lá trên tay cùng màu với lá bạn đã bỏ.

### Khuê Tú — `guixiu`

• Sau khi mở tướng này, bạn có thể rút 2 lá.
• Sau khi tướng này bị loại bỏ, bạn có thể hồi 1 máu.

### Tồn Tự — `cunsi`

Giai đoạn ra bài, nếu bạn đã mở tướng này, bạn có thể chọn 1 người, thực hiện lần lượt:
- Bạn loại bỏ tướng này;
- Họ nhận kỹ năng »Dũng Quyết«;
- Nếu họ không phải bạn, họ rút 2 lá bài.

### Dũng Quyết — `yongjue`

Sau khi kết toán xong [Sát] do người cùng thế lực với bạn sử dụng trong giai đoạn ra bài của họ, nếu lá này là lá đầu tiên họ sử dụng trong giai đoạn này, bạn có thể lệnh họ thu lấy lá [Sát] này.

### Hùng Dũng — `jiang`

Sau khi bạn xác định hoặc trở thành mục tiêu của [Sát] Đỏ hoặc [Quyết đấu], bạn có thể rút 1 lá.

### Ưng Dương — `yingyang`

Sau khi mở lá đấu điểm của bạn, bạn có thể lệnh lá này +3 hoặc -3 điểm trong lần đấu điểm này (Lớn nhất là K, nhỏ nhất là A).

### Hồn Thương — `hunshang`

Phó tướng kỹ, Giảm 0.5 máu gốc: Khi bắt đầu giai đoạn chuẩn bị, nếu số máu của bạn là 1, trong lượt này, bạn có kỹ năng »Anh Tư« và »Anh Hồn«.

### Đoạn Tiết — `duanxie`

Một lần trong giai đoạn ra bài, bạn có thể lệnh X người không trong trạng thái xích nhận trạng thái xích (X là số máu đã mất của bạn, tối thiểu 1), sau đó bạn nhận trạng thái xích.

### Phấn Mệnh — `fenming`

Khi bắt đầu giai đoạn kết thúc, nếu bạn trong trạng thái xích, bạn có thể bỏ đi 1 lá của những người trong trạng thái xích.

### Hoàng Chinh — `hengzheng`

Khi bắt đầu giai đoạn rút bài, nếu số máu của bạn là 1 hoặc không có bài trên tay, bạn có thể không rút bài, thu lấy từ mỗi người khác 1 lá trong vùng chơi.

### Bạo Lăng — `baoling`

Chủ tướng kỹ, Tỏa định kỹ: Khi bạn kết thúc giai đoạn ra bài, nếu bạn đã mở tướng này và có phó tướng, bạn thực hiện lần lượt:
- Bạn loại bỏ phó tướng;
- Bạn tăng giới hạn máu thêm 3, hồi 3 máu;
- Bạn mất kỹ năng này và nhận kỹ năng »Băng Hoại«

### Băng Hoại — `benghuai`

Tỏa định kỹ: Khi bắt đầu giai đoạn kết thúc, nếu bạn không phải là người có số máu thấp nhất, bạn chọn mất 1 máu hoặc giảm 1 giới hạn máu.

### Xuyên Tâm — `chuanxin`

Giai đoạn ra bài của bạn, khi bạn gây sát thương cho mục tiêu của [Sát] hoặc [Quyết Đấu], nếu họ có thế lực xác định khác với bạn (bạn có thể mở tướng này để xác định thế lực) và có Phó tướng, bạn có thể chặn sát thương này, lệnh mục tiêu chọn 1 mục:
1. Nếu họ có trang bị, họ bỏ toàn bộ bài trong vùng Trang Bị và mất 1 máu.
2. Họ loại bỏ Phó tướng.

### Phong Thỉ — `fengshi`

Trận pháp kỹ: Quan hệ vây công: Nếu bạn là người vây công, sau khi người vây công xác định mục tiêu của lá [Sát], ứng với mỗi mục tiêu, nếu mục tiêu này là người bị vây công, bạn lệnh họ bỏ 1 lá trong vùng trang bị.

### Ngộ Tâm — `wuxin`

Khi bắt đầu giai đoạn rút bài, có thể xem X lá đầu chồng bài rút và sắp xếp tùy ý những lá này lên đầu chồng bài rút (X là số người cùng thế lực với bạn).

### Hoằng Pháp — `hongfa`

Quân chủ kỹ, Tỏa định kỹ: Bạn có »Hoàng Cân Thiên Bình Phủ«.

»Hoàng Cân Thiên Bình Phủ«:
• Khi bắt đầu giai đoạn chuẩn bị, nếu bạn không có [Thiên Binh], bạn lấy X lá đầu chồng bài rút đặt ngửa lên tướng này, gọi là [Thiên Binh] (X là số người cùng thế lực với bạn).
• Khi bạn tính toán số người cùng thế lực với bạn, +1 với mỗi [Thiên Binh].
• Khi bạn mất máu, bạn có thể đưa 1 [Thiên Binh] vào chồng bài bỏ, chặn việc mất máu.
• Người thế lực Quần có thể chuyển hóa sử dụng/đánh ra [Thiên Binh] thành [Sát].

### Hoàng Cân Thiên Bình Phủ — `huangjinsymbol`

• Khi bắt đầu giai đoạn chuẩn bị, nếu bạn không có [Thiên Binh], bạn lấy X lá đầu chồng bài rút đặt ngửa lên tướng này, gọi là [Thiên Binh] (X là số người cùng thế lực với bạn).
• Khi bạn tính toán số người cùng thế lực với bạn, +1 với mỗi [Thiên Binh].
• Khi bạn mất máu, bạn có thể đưa 1 [Thiên Binh] vào chồng bài bỏ, chặn việc mất máu.
• Người thế lực Quần có thể chuyển hóa sử dụng/đánh ra [Thiên Binh] thành [Sát].

### Vấn Đạo — `wendao`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 1 lá Đỏ ngoại trừ [Thái Bình Yêu Thuật] và thu lấy [Thái Bình Yêu Thuật] trong chồng bài bỏ hoặc trên bàn chơi.

### Thái Bình Yêu Thuật — `PeaceSpell`

Bài trang bị - Phòng cụ

Kỹ năng: Tỏa định kỹ:

• Khi bạn nhận sát thương có thuộc tính, bạn chặn sát thương này.

• Giới hạn trữ bài của bạn +X (X là số người cùng thế lực với bạn).

• Khi bạn mất đi [Thái Bình Yêu Thuật] từ vùng trang bị, bạn rút 2 lá, sau đó nếu máu của bạn > 1, bạn mất 1 máu.


## NewSGSPackage

Nguồn: `lang\vi_VN\Package\NewSGSPackage.lua`

Tên nhân vật nhận diện được: Tưởng Cán (`jianggan`); Dương Uyển (`yangwan`); Chu Di (`zhouyi`); Lữ Linh Khởi (`lvlingqi`); Nam Hoa Lão Tiên (`nanhualaoxian`).

### Ngụy Thành — `weicheng`

Khi bài trên tay bạn chuyển đến tay người khác, nếu bài trên tay bạn ít hơn số máu hiện tại, bạn có thể rút 1 lá.

### Đạo Thư — `daoshu`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 chất và 1 người có bài trên tay, thu lấy 1 lá bài trên tay người đó và so sánh với chất bài đã đoán:
* Trùng: Bạn gây 1 sát thương cho họ và tăng thêm 1 lần sử dụng kỹ năng trong giai đoạn này;
* Không trùng: Bạn giao 1 lá bài trên tay có chất khác với lá bạn nhận cho họ, nếu không thể, mở toàn bộ bài trên tay.

### Dụ Ngôn — `youyan`

Một lần trong lượt của bạn, sau khi bài của bạn tiến vào chồng bài bỏ do bỏ bài, bạn có thể lật ra 4 lá trên đầu chồng bài và thu lấy những lá khác chất với những lá bạn đã bỏ trong lần này.

### Truy Hoàn — `zhuihuan`

Khi bạn kết thúc lượt, bạn có thể chọn tối đa 2 người, lệnh mỗi người nhận 1 [Truy Hoàn] khác nhau đến khi bắt đầu lượt tiếp theo của bạn (Không ai được biết loại [Truy Hoàn] đã nhận);
▶ Sau khi họ nhận sát thương, họ bỏ đi [Truy Hoàn], nếu [Truy Hoàn] đã bỏ là:
* [Sát thương]: Họ gây 1 sát thương cho nguồn sát thương;
* [Bỏ bài]: Nguồn sát thương bỏ 2 lá trên tay.

### Trục Khấu — `zhukou`

Trong lượt của mỗi người, sau khi bạn gây sát thương lần đầu tiên trong giai đoạn ra bài của họ, bạn có thể rút X lá (X là số lá bạn đã sử dụng trong lượt này, tối đa 5).

### Đoạn Niệm — `duannian`

Khi kết thúc giai đoạn ra bài, nếu bạn có bài trên tay, bạn có thể bỏ tất cả bài trên tay, sau đó bổ sung bài đến giới hạn máu.

### Liên Hựu — `lianyou`

Khi bạn trận vong, bạn có thể lệnh cho 1 người khác nhận kỹ năng »Hưng Hỏa«

### Hưng Hỏa — `xinghuo`

Tỏa định kỹ: Khi bạn gây sát thương Hỏa, sát thương này +1.

### Quắc Vũ — `guowu`

Khi bắt đầu giai đoạn ra bài, bạn có thể mở tất cả bài trên tay, căn cứ vào số loại bài bạn có mà bạn nhận hiệu quả tương ứng:
* 1+: Bạn thu lấy 1 lá [Sát] ngẫu nhiên từ chồng bài bỏ;
* 2+: Trong giai đoạn này, bạn sử dụng bài không giới hạn khoảng cách;
* 3+: Một lần trong giai đoạn này, sau khi bạn chỉ định mục tiêu của [Sát], bạn có thể chỉ định thêm tối đa 2 mục tiêu.

### Trang Nhung — `zhuangrong`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 1 lá công cụ, bạn nhận kỹ năng »Vô Song« trong giai đoạn này.

### Thần Uy — `shenwei`

Chủ tướng kỹ, Tỏa định kỹ, Giảm 0.5 máu gốc:
• Giới hạn trữ bài trên tay bạn +2;
• Giai đoạn rút bài, nếu bạn là người có số máu lớn nhất, số lá bạn rút +2.

### Cộng Tu — `gongxiu`

Giai đoạn rút bài, bạn có thể rút ít đi 1 lá, sau đó lựa chọn tối đa X người (X là giới hạn máu của bạn), bạn chọn 1 mục:
1. Họ rút 1 lá;
2. Họ bỏ 1 lá;
▷ Không thể liên tiếp lựa chọn cùng 1 mục.

### Kinh Hợp — `jinghe`

Một lần trong giai đoạn ra bài, bạn có thể mở tối đa X lá trên tay (X là giới hạn máu của bạn) và chọn số người tương đương có tướng đã mở; bạn mở ra ngẫu nhiên số kỹ năng bằng số người đã chọn, mỗi người có thể chọn và nhận 1 kỹ năng trong đó đến khi bắt đầu lượt tiếp theo của bạn.

### Lôi Kích — `leiji_tianshu`

Khi bạn sử dụng/đánh ra [Thiểm], bạn có thể lệnh 1 người khác tiến hành phán xét, nếu kết quả phán xét có chất BÍCH, bạn gây 2 sát thương Lôi cho họ.

### Âm Binh — `yinbing`

Tỏa định kỹ:
• Khi bắt đầu kết toán hiệu quả của [Sát], sửa hiệu quả thành mục tiêu mất X máu (X là số sát thương).
• Sau khi người khác mất máu, bạn rút 1 lá.

### Hoạt Khí — `huoqi`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 1 lá và chọn 1 người có ít máu nhất, lệnh họ hồi 1 máu và rút 1 lá.

### Quỷ trợ — `guizhu`

Một lần trong lượt của mỗi người, khi 1 người tiến vào trạng thái hấp hối, bạn có thể rút 2 lá.

### Tiên Thụ — `xianshou`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người:
* Nếu họ đã bị thương, họ rút 1 lá;
* Nếu không, họ rút 2 lá.

### Luận Đạo — `lundao`

Sau khi nhận sát thương, nếu số bài trên tay nguồn sát thương so với bạn:
* Nhiều hơn: Bạn có thể bỏ 1 lá của họ;
* Ít hơn: Bạn có thể rút 1 lá.

### Quan Nguyệt — `guanyue`

Khi bắt đầu giai đoạn kết thúc, bạn có thể xem 2 lá trên đầu chồng bài rút, thu lấy 1 lá trong số đó.

### Ngôn Chính — `yanzheng`

Khi bắt đầu giai đoạn chuẩn bị, nếu số bài trên tay bạn > 1, bạn có thể giữ lại 1 lá và bỏ đi số lá còn lại và chọn tối đa X người (X là số lá đã bỏ), bạn gây 1 sát thương cho họ.

## Overseas

Nguồn: `lang\vi_VN\Package\Overseas.lua`

Tên nhân vật nhận diện được: Himiko (`beimihu`); Tào Chân (`caozhen`); Liêu Hóa (`liaohua`); Gia Cát Cẩn (`zhugejin`); Toàn Tông (`quancong`); Quách Hoài (`guohuai`); Dương Tu (`yangxiu`); Tổ Mậu (`zumao`); Phục Hoàn (`fuwan`); Trần Đáo (`chendao`); Điền Dự (`tianyu`); Mã Lương (`maliang`); Hoa Hùng (`huaxiong`); Trương Xuân Hoa (`zhangchunhua`); Lưu Phu Nhân (`liufuren`); Y Tịch (`yijibo`); Trương Dực (`zhangyi`); Trình Phổ (`chengpu`); Trình Dục (`chengyu`); Hạ Hầu Thượng (`xiahoushang`); Cố Ung (`guyong`); Lý Nghiêm (`liyan`); Mã Hưu & Mã Thiết (`maxiumatie`); Tào Ngang (`caoang`); Chu Hoàn (`zhuhuan`); Trần Đăng (`chendeng`); Thạch Thao (`shitao`); Tiềm Học (`qianxue`); Tôn Hoàn (`sunhuan`); Công Tôn Toản (`gongsunzan`).

### Quỷ Thuật — `guishu`

Bạn có thể chuyển hóa sử dụng 1 lá BÍCH trên tay thành [Tri Bỉ Tri Kỷ]/[Viễn Giao Cận Công];
▷ Bạn cần sử dụng xen kẽ 2 lá trên theo cách này trong cùng 1 lượt.

### Viễn Vực — `yuanyu`

Tỏa định kỹ: Khi bạn tính toán sát thương phải nhận, nếu bạn không thuộc tầm đánh của nguồn sát thương, sát thương này -1.

### Ty Địch — `sidi`

• Sau khi người cùng thế lực với bạn nhận sát thương, nếu họ có bài và số loại [Ngự] của bạn < 3, bạn có thể phát động kỹ năng, họ có thể đặt 1 lá của họ lên tướng của bạn, gọi là [Ngự] (Không thể chọn lá cùng loại với những [Ngự] đã có).
• Sau khi bắt đầu lượt của người thế lực khác bạn, bạn có thể đưa tối đa 3 [Ngự] vào chồng bài bỏ, đưa ra số lựa chọn khác nhau tương ứng với mỗi [Ngự]:
1. Bạn chọn 1 loại bài có cùng loại với 1 trong số [Ngự] vừa bỏ, họ không thể sử dụng loại bài này trong lượt này;
2. Bạn chọn 1 kỹ năng của tướng đã mở của họ, vô hiệu kỹ năng đó trong lượt này;
3. Bạn lệnh họ chọn 1 người khác có cùng thế lực với bạn, người này hồi 1 màu.

### Đương Tiên — `dangxian`

Tỏa định kỹ:
• Sau khi bạn mở tướng này lần đầu tiên, bạn nhận 1 tiêu ký [Tiên Khu].
• Sau khi bắt đầu lượt, bạn nhận 1 giai đoạn ra bài.

### Hoãn Thích — `huanshi`

Khi phán xét của người cùng thế lực với bạn có hiệu lực, bạn có thể đánh ra 1 lá để thay thế kết quả phán xét đó.

### Hoằng Viện — `hongyuan`

•Khi bạn rút bài vì hiệu quả của »Hợp Tung«, bạn có thể lệnh 1 người khác có cùng thế lực với bạn rút bài thay bạn.
• Một lần trong giai đoạn ra bài, bạn có thể mở 1 lá trên tay, lá đó khi ở trên tay bạn trong giai đoạn này xem như có ký hiệu »Hợp Tung«.

### Minh Triết — `mingzhe`

Ngoài lượt của bạn:
• Khi bạn sử dụng/đánh ra lá Đỏ, bạn có thể rút 1 lá.
• Khi bạn mất đi bài trong vùng trang bị, nếu trong đó có lá Đỏ, bạn có thể rút 1 lá

### Thân Trùng — `qinzhong`

Phó tướng kỹ: Sau khi bắt đầu lượt, bạn có thể hoán đổi phó tướng của bạn với 1 người cùng thế lực với bạn.

### Chiêu Phụ — `zhaofu`

• Khi bắt đầu giai đoạn ra bài, nếu tổng số [Thưởng] của tất cả người khác < 3, bạn có thể bỏ 1 lá và chọn 1 người khác, họ tăng 1 [Thưởng].
• Sau khi lá cơ bản/công cụ phổ thông do người có [Thưởng] sử dụng kết toán xong, bạn có thể lệnh họ giảm 1 [Thưởng], xem như bạn sử dụng lá đó.

### Tinh Sách — `jingce`

Giai đoạn ra bài, sau khi lá thứ X do bạn sử dụng kết toán xong (X là số máu hiện tại của bạn), nếu không có ai đang giải quyết hấp hối, bạn có thể yêu cầu 1 người thế lực xác định khác bạn chấp hành 1 [Quân Lệnh], nếu họ không chấp hành, bạn rút 2 lá.

### Đạm Lạc — `danlao`

Sau khi bạn trở thành mục tiêu của lá công cụ, nếu số mục tiêu của lá này > 1, bạn có thể rút 1 lá, sau đó lệnh lá này không có hiệu quả với bạn.

### Kê Lặc — `jilei`

Sau khi bạn nhận sát thương, nếu sát thương này có nguồn, bạn có thể chọn 1 loại bài, lệnh nguồn sát thương trong lượt này không thể sử dụng, đánh ra hoặc bỏ lá trên tay thuộc loại bài này.

### Dẫn Binh — `yinbingx`

• Khi bắt đầu giai đoạn kết thúc, bạn có thể đặt tùy ý lá phi cơ bản lên tướng này, gọi là [Trách].
• Sau khi bạn nhận sát thương từ [Sát] hoặc [Quyết Đấu], bạn bỏ 1 [Trách].

### Tuyệt Địa — `juedi`

Tỏa định kỹ:
• Thần lực luôn ở bên bạn.
• Khi bắt đầu giai đoạn chuẩn bị, nếu bạn có [Trách], bạn chọn 1 mục:
1. Bỏ tất cả lá [Trách], bổ sung bài trên tay tới giới hạn máu;
2. Giao tất cả [Trách] cho 1 người khác có số máu ≤ bạn, lệnh họ hồi 1 máu và rút bài bằng số [Trách] bạn đã giao.

### Mưu Hội — `moukui`

Sau khi bạn xác định mục tiêu của [Sát], ứng với mỗi mục tiêu, bạn có thể chọn 1 mục:
1. Rút 1 lá;
2. Bỏ 1 lá của mục tiêu của [Sát] này;
▶ Sau khi [Sát] này bị triệt tiêu bởi [Thiểm] của mục tiêu, họ bỏ 1 lá của bạn.

### Vãng Liệt — `wanglie`

• Lá đầu tiên bạn sử dụng trong giai đoạn ra bài không giới hạn khoảng cách.
• Giai đoạn ra bài, khi bạn sử dụng [Sát] hoặc công cụ phổ thông, bạn có thể lệnh cho tất cả mọi người không được hưởng ứng với lá này; nếu làm vậy, bạn không thể sử dụng bài trong giai đoạn này.

### Địa Tải — `dizai`

Trận pháp kỹ: Quan hệ vây công: Nếu bạn là người vây công, khi người vây công gây sát thương cho mục tiêu bị vây công của lá [Sát], người vây công còn lại có thể bỏ 1 lá để lệnh sát thương này +1.

### Chấn Tập — `zhenxi`

Sau khi bạn xác định mục tiêu của [Sát], ứng với mỗi mục tiêu, bạn có thể chọn 1 mục:
1. Bạn bỏ 1 lá của họ;
2. Bạn chuyển hóa sử dụng 1 lá TÉP phi công cụ thành [Binh Lương Thốn Đoạn] hoặc 1 lá RÔ phi công cụ thành [Lạc Bất Tư Thục] không giới hạn khoảng cách với họ;
▷ Nếu bạn đã mở 2 tướng và họ có tướng đang úp, bạn có thể chấp hành cả 2 mục với thứ tự tùy ý.

### Kiệm Tố — `jiansu`

Phó tướng kỹ, Giảm 0.5 máu gốc:
• Khi bạn nhận bài ngoài lượt, bạn có thể gọi những lá này trên tay bạn là [Kim] chừng nào lá đó còn trên tay bạn, [Kim] luôn công khai với những người khác.
• Khi bắt đầu giai đoạn ra bài, bạn có thể bỏ đi tùy ý [Kim], sau đó chọn 1 người đã bị thương có số máu ≤ số [Kim] đã bỏ, lệnh họ hồi 1 máu.

### Mục Minh — `mumeng`

Một lần trong giai đoạn ra bài, bạn có thể chuyển hóa sử dụng 1 lá CƠ trên tay thành [Viễn Giao Cận Công]/[Lục Lực Đồng Tâm]

### Nạp Man — `naman`

Khi người khác sử dụng bài Đen có chỉ định nhiều mục tiêu, bạn có thể tiến hành phán xét, nếu kết quả phát xét không phải BÍCH, bạn chọn 1 mục:
1. Lệnh 1 người khác trở thành mục tiêu của bài (Không bị giới hạn khoảng cách);
2. Hủy bỏ mục tiêu đối với 1 mục tiêu của lá đó.

### Diệu Võ — `yaowu`

Hạn định kỹ: Sau khi bạn gây sát thương, nếu tướng này đang úp mặt, bạn có thể phát động kỹ năng này: Bạn tăng 2 giới hạn máu, hồi 2 máu;
▶ Sau khi bạn trận vong, tất cả người cùng thế lực với bạn mất 1 máu.

### Thị Dũng — `shiyong`

Tỏa định kỹ: Khi bạn tính toán sát thương phải nhận từ lá bài:
* Nếu bạn chưa phát động »Diệu Võ« và lá gây ra sát thương không phải màu Đỏ, bạn rút 1 lá;
* Nếu bạn đã phát động »Diệu Võ« và lá gây sát thương không phải màu Đen, nguồn sát thương rút 1 lá.

### Quả Quyết — `guojue`

• Sau khi bạn mở tướng này lần đầu tiên, bạn gây 1 sát thương cho 1 người khác.
• Khi 1 người khác tiến vào trạng thái hấp hối do bạn gây sát thương, bạn có thể bỏ 1 lá của họ.

### Thương Thệ — `shangshi`

Sau khi bạn nhận sát thương, bạn có thể chọn bỏ 1 lá hoặc giao X lá trên tay bạn cho 1 người khác; nếu làm vậy, bạn rút X lá (X lá số máu bạn đã mất).

### Truy Đố — `zhuidu`

Một lần trong giai đoạn ra bài, khi bạn gây sát thương, bạn có thể lệnh người nhận sát thương chọn 1 mục:
1. Sát thương này +1;
2. Nếu họ có lá trong vùng trang bị, bỏ đi tất cả bài trong vùng trang bị;
▷ Nếu họ có giới tính nữ, bạn có thể bỏ 1 lá, lệnh họ thực hiện cả 2 mục.

### Kỳ Cung — `shigong`

Hạn định kỹ: Ngoài lượt của bạn, khi bạn tiến vào trạng thái hấp hối, bạn có thể loại bỏ Phó tướng của bạn, sau đó lệnh người đang có lượt chọn 1 mục:
1. Họ nhận 1 kỹ năng không phân loại từ lá tướng mà bạn vừa loại bỏ, lệnh bạn hồi đầy máu;
2. Lệnh bạn hồi đến 1 máu.

### Định Khoa — `dingke`

Một lần trong lượt của mỗi người, sau khi 1 người cùng thế lực với bạn mất bài ngoài lượt không vì sử dụng/đánh ra, bạn có thể chọn 1 mục:
1. Giao 1 lá trên tay cho họ;
2. Lệnh người đang có lượt bỏ 1 lá trên tay;
▷ Nếu số [Âm dương ngư] của bạn nhỏ hơn giới hạn máu, bạn thu lấy 1 tiêu ký [Âm dương ngư].

### Cấp Viện — `jiyuan`

Khi có người tiến vào trạng thái hấp hối hoặc sau khi có người được bạn giao bài do phát động »Định Khoa«, bạn có thể lệnh họ rút 1 lá.

### Kháng Nhuệ — `kangrui`

Một lần trong giai đoạn ra bài của 1 người cùng thế lực với bạn, khi họ sử dụng bài có chỉ định 1 người khác làm mục tiêu duy nhất, bạn có thể hủy bỏ mục tiêu của lá đó, lệnh họ chọn 1 mục:
1. Bổ sung bài trên tay đến X lá (X là số máu của họ), giai đoạn này, họ không thể chỉ định người ngoài họ làm mục tiêu của bài;
2. Nếu không có người trong trạng thái hấp hối, lệnh mục tiêu ban đầu của lá đó xem như sử dụng [Quyết đấu] với họ, số sát thương của [Quyết đấu] này +1.

### Hổ Huân — `huxun`

Khi 1 người kết thúc lượt, nếu trong lượt này có người tiến vào trạng thái hấp hối do bạn gây sát thương, bạn có thể chọn 1 mục:
1. Nếu bạn không phải người duy nhất có giới hạn máu cao nhất, bạn tăng 1 giới hạn máu và hồi 1 máu;
2. Bạn có thể di chuyển 1 lá trên bàn chơi.

### Nguyên Tòng — `yuancong`

Khi kết thúc giai đoạn ra bài của 1 người cùng thế lực với bạn, nếu trong giai đoạn này họ không gây sát thương, họ có thể giao 1 lá cho bạn, sau đó bạn có thể sử dụng 1 lá trên tay.

### Phục Binh — `shefu`

• Một lần trong giai đoạn ra bài, bạn có thể đặt 1 lá trên tay lên tướng của bạn, gọi là [Phục Binh].
• Khi 1 người khác sử dụng bài trên tay, bạn có thể đưa 1 [Phục Binh] có cùng tên với lá đó vào chồng bài bỏ, hủy bỏ hoàn toàn lá đó.
• Khi bắt đầu giai đoạn chuẩn bị, nếu số [Phục Binh] > 2, bạn đưa số [Phục Binh] vào chồng bài bỏ đến khi còn 2.

### Bí Dục — `benyu`

Sau khi bạn nhận sát thương:
* Nếu bài trên tay bạn ít hơn nguồn sát thương, bạn chọn 1 mục:
1. Bổ sung bài trên tay đến khi bằng với họ, tối đa 5 lá;
2. Lệnh họ bỏ đi bài trên tay đến khi bằng bạn, tối đa bỏ 5 lá.
* Nếu bài trên tay bạn nhiều hơn nguồn sát thương, bạn có thể bỏ số bài trên tay bằng số bài trên tay họ +1, sau đó gây 1 sát thương cho họ.

### Tham Phong — `tanfeng`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể bỏ 1 lá trong vùng chơi của 1 người thế lực khác bạn;
▷ Họ có thể chọn nhận 1 sát thương Hỏa từ bạn để lệnh bạn bỏ qua 1 giai đoạn trong lượt này, ngoại trừ giai đoạn chuẩn bị.

### Lễ Phụ — `lifu`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người, lệnh họ bỏ 2 lá, sau đó bạn xem lá trên đầu chồng bài rút và giao cho họ.

### Ngôn Trung — `yanzhong`

Khi bắt đầu giai đoạn kết thúc, bạn có thể chọn 1 chất và chọn 1 người khác có bài trên tay, bạn bỏ 1 lá trên tay họ; nếu chất của lá đã bỏ và chất đã đoán:
* Khác chất: bạn bỏ 1 lá;
* Cùng chất và chất đó là:
CƠ: Bạn hồi 1 máu;
RÔ: Bạn rút 1 lá, loại bỏ trạng thái xích;
TÉP: Họ giao 1 lá cho bạn;
BÍCH: Họ mất 1 máu.

### Căng Võ — `jinwu`

Khi bắt đầu giai đoạn ra bài, bạn có thể yêu cầu bạn chấp hành 1 quân lệnh:
* Nếu chấp hành, bạn xem như sử dụng 1 [Sát];
* Nếu không chấp hành, bạn kết thúc giai đoạn này.

### Trúc Khoa — `zhuke`

Chủ tướng kỹ, Giảm 0.5 máu gốc:
• Sau khi bạn chọn chấp hành quân lệnh, bạn có thể chọn lại quân lệnh để chấp hành.
• Khi bạn nhận trạng thái xích hoặc trạng thái chồng tướng, bạn có thể lệnh 1 người cùng thế lực với bạn hồi 1 máu.

### Khuyến Giá — `quanjia`

Phó tướng kỹ: Sau khi bạn mở tướng này lần đầu tiên, bạn phát động kỹ năng này, thực hiện lần lượt:
- Triệu hoán thế lực, có thể hưởng ứng triệu hoán này mà không trở thành dã tâm;
- Người cùng thế lực với bạn rút 1 lá
- Người có kỹ năng »Nhân Đức« nhận kỹ năng »Chương Vũ« và »Thụ Việt«

### Khẩn Thương — `kenshang`

Bạn có thể chuyển hóa sử dụng tùy ý số lá của bạn thành [Sát] (ít nhất 1 lá);
▶ Sau khi bạn chỉ định mục tiêu cho [Sát] này, bạn có thể lệnh tất cả người khác ở ngoài tầm đánh của bạn trở thành mục tiêu của [Sát] này (không giới hạn khoảng cách), hủy bỏ tất cả mục tiêu trong tầm đánh của bạn;
▶ Sau khi lá [Sát] này kết toán, nếu số lá bạn đã đem sử dụng > X, bạn rút X lá; Ngược lại, bạn mất »Mã Thuật« hoặc »Khẩn Thương« (X là tổng số sát thương mà [Sát] này đã gây ra).

### Hiếu Liêm — `xiaolian`

• Sau khi mở tướng này lần đầu, bạn có thể di chuyển 1 trang bị trên bàn chơi; sau đó, bạn có thể lặp lại quá trình này thêm 1 lần.
• Sau khi tướng này bị loại bỏ, người cùng thế lực với bạn rút 1 lá.

### Khảng Khái — `kangkai`

Sau khi 1 người cùng thế lực với bạn trở thành mục tiêu của [Sát], bạn có thể loại bỏ tướng này, thực hiện lần lượt:
- Chọn 1 người, lệnh họ nhận kỹ năng »Phi Ảnh«;
- Nếu người đó không phải là bạn, người đó hồi 1 máu và thoát trạng thái xích.

### Cự Thiên — `jutian`

Một lần trong lượt của mỗi người đối với mỗi mục lựa chọn, sau khi bạn gây sát thương cho người khác, bạn có thể chọn 1 mục:
1. Bạn chọn 1 người cùng thế lực với người đã nhận sát thương, lệnh họ bỏ bài trên tay đến khi bằng với số máu của họ, tối đa bỏ 5 lá;
2. Bạn chọn 1 người cùng thế lực với bạn, lệnh họ bổ sung bài trên tay đến giới hạn máu của họ.

### Hào Khôi — `haokui`

Khi bắt đầu giai đoạn ra bài, bạn có thể rút 2 lá;
▶ Khi có bài tiến vào chồng bài bỏ trong giai đoạn bỏ bài lượt này, bạn đem những lá này giao cho 1 người thế lực xác định khác bạn, ưu tiên theo thứ tự sau:
* Người thuộc đại thế lực;
* Người có số máu lớn nhất trong số những người thế lực xác định khác bạn;
▶ Khi kết thúc lượt này, nếu bạn không giao bài cho người khác bởi kỹ năng này, bạn thực hiện lần lượt:
- Nếu bạn đã mở tất cả tướng, bạn có thể úp tướng này;
- Bạn có thể chọn 1 người cùng thế lực với bạn, họ có thể đổi Phó tướng.

### Hư Thực — `xushi`

Khi bạn trở thành mục tiêu duy nhất của bài do người khác sử dụng, nếu tướng này đang úp, bạn có thể hủy bỏ mục tiêu đối với bạn;
▷ Bạn lệnh họ bỏ 1 lá.

### Kiếm Ca — `jiange`

Bạn có thể chuyển hóa sử dụng/đánh ra lá phi cơ bản thành [Sát].

### Tiềm Học — `qianxue`

Chủ tướng kỹ, Giảm 0.5 máu gốc: Khi 1 người kết thúc lượt, bạn có thể thu lấy tối đa X lá trong những lá đã tiến vào chồng bài bỏ trong lượt này (X là số vùng của bạn mà đã mất đi lá cuối cùng trong lượt này);
▶ Bạn cần ưu tiên thu lấy những lá phi cơ bản trước;
▶ Bạn không thể thu lấy [Hiệp Thiên Tử Dĩ Lệnh Chư Hầu].

### Trục Cốc — `zhuhu`

Tỏa định kỹ: Sau khi người cùng thế lực với bạn đổi Phó tướng hoặc trận vong, nếu vị trí của tướng này là:
- Chủ tướng và tướng còn lại của bạn là tướng đơn thế lực: Bạn hoán đổi Chủ tướng và Phó tướng
- Phó tướng: Bạn thoát khỏi trạng thái xích;
▶ Bạn đổi Phó tướng.

### Nghịch Trảm — `nizhan`

Khi kết thúc lượt của người khác, nếu bạn đã triệt tiêu lá bài do họ sử dụng trong lượt này hoặc bạn đã mất đi lá cuối cùng trên tay, bạn có thể chọn 1 mục:
1. Bạn thu lấy 1 lá của họ;
2. Bạn xem như sử dụng 1 [Sát] Bỏ qua phòng cụ với họ;

### Khu Thỉ — `qushi`

Tỏa định kỹ: Giai đoạn ra bài của bạn, sau khi lá [Sát] do bạn sử dụng kết toán xong, nếu [Sát] này đã bị triệt tiêu, bạn lệnh giới hạn sử dụng [Sát] và số mục tiêu của [Sát] do bạn sử dụng trong giai đoạn này +1.

### Nhạn Hàng — `yanxing`

Trận pháp kỹ: Quan hệ đội hình: Nếu bạn có trong quan hệ đội hình, khoảng cách từ người cùng đội hình với bạn đến người khác -X (X là số người khác có cùng đội hình với bạn).

### Nghĩa Tòng — `yicong`

Chủ tướng kỹ, Giảm 0.5 máu gốc: Sau khi lá [Sát] do người khác có cùng thế lực với bạn sử dụng kết toán xong, nếu [Sát] này đã bị triệt tiêu, họ có thể lệnh bạn thu lấy [Sát] này.

## PowerPackage

Nguồn: `lang\vi_VN\Package\PowerPackage.lua`

Tên nhân vật nhận diện được: Thôi Diễm & Mao Giới (`cuiyanmaojie`); Vu Cấm (`yujin`); Vương Bình (`wangping`); Pháp Chính (`fazheng`); Ngô Quốc Thái (`wuguotai`); Lục Kháng (`lukang`); Viên Thuật (`yuanshu`); Trương Tú (`zhangxiu`); Tào Tháo - Quân (`lord_caocao`); Gây sát thương (`command1`); Rút 1, đưa 2 (`command2`); Mất máu (`command3`); Khóa bài, kỹ năng (`command4`); Chồng tướng, cấm hồi máu (`command5`); Giữ 1 trên tay, 1 trang bị (`command6`).

### Chinh Tịch — `zhengbi`

Khi bắt đầu giai đoạn ra bài, bạn có thể chọn 1 mục:
1. Chọn 1 người khác không có thế lực, bạn sử dụng bài với họ không giới hạn khoảng cách và số lần đến sau khi kết thúc lượt này hoặc sau khi họ lật tướng;
2. Chọn 1 người khác đã có thế lực, bạn giao cho họ 1 lá cơ bản, lệnh họ giao cho bạn 2 lá cơ bản hoặc 1 lá phi cơ bản.

### Phụng Nghênh — `fengying`

Hạn định kỹ: Bạn có thể chuyển hóa sử dụng tất cả bài trên tay thành [Hiệp Thiên Tử Dĩ Lệnh Chư Hầu] (Bỏ qua yêu cầu Đại thế lực);
▶ Khi bạn sử dụng [Hiệp Thiên Tử Dĩ Lệnh Chư Hầu] này, bạn lệnh tất cả người cùng thế lực với bổ sung bài trên tay đến giới hạn máu.

### Tiết Viện — `jieyue`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể giao 1 lá trên tay cho 1 người không phải thế lực Ngụy, sau đó yêu cầu họ chấp hành 1 [Quân Lệnh]:
* Nếu họ chấp hành, bạn rút 1 lá;
* Nếu không, giai đoạn rút bài lượt này, bạn rút thêm 3 lá.

### Tướng Lược — `jianglve`

Hạn định kỹ: Giai đoạn ra bài, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Bạn chọn 1 [Quân Lệnh], yêu cầu tất cả người khác có cùng thế lực với bạn chấp hành [Quân Lệnh] này;
- Bạn và những người đã chọn chấp hành [Quân Lệnh] tăng 1 giới hạn máu, hồi 1 máu;
- Bạn rút X lá (X là số người đã hồi máu từ kỹ năng này).

### Ân Oán — `enyuan`

Tỏa định kỹ:
• Sau khi bạn trở thành mục tiêu của [Đào] do người chơi khác sử dụng, họ rút 1 lá.
• Sau khi bạn nhận sát thương, nguồn gây sát thương chọn giao 1 lá trên tay cho bạn hoặc mất 1 máu.

### Huyễn Hoặc — `xuanhuo`

Một lần trong giai đoạn ra bài của người khác có cùng thế lực với bạn, họ có thể giao cho bạn 1 lá trên tay, sau đó họ có thể bỏ 1 lá và lựa chọn nhận 1 trong các kỹ năng sau mà chưa có trên bàn cho đến hết lượt hoặc tướng có kỹ năng tương ứng được mở: »Võ Thánh«, »Bào Hao«, »Long Đảm«, »Thiết Kỵ«, »Liệt Cung«, »Cuồng Cốt«.

### Cam Lộ — `ganlu`

Một lần trong giai đoạn ra bài, bạn có thể chọn 2 người có số bài trong vùng trang bị không cùng bằng 0 và số chênh lệch ≤ số máu bạn đã mất, hoán đổi bài trong vùng trang bị của 2 người này.

### Bổ Ích — `buyi`

Một lần trong lượt của mỗi người, sau khi người cùng thế lực với bạn thoát khỏi trạng thái hấp hối, bạn có thể yêu cầu nguồn sát thương chấp hành 1 [Quân Lệnh], nếu họ không chấp hành, người vừa thoát khỏi trạng thái hấp hối hồi 1 máu.

### Khắc Thủ — `keshou`

Khi bạn tính toán sát thương phải nhận, bạn có thể bỏ 2 lá có cùng màu, lệnh sát thương này -1;
▷ Nếu không có người khác có cùng thế lực với bạn, bạn tiến hành phán xét, nếu kết quả phán xét có màu Đỏ, bạn rút 1 lá.

### Trác Vi — `zhuwei`

Sau khi phán xét của bạn có hiệu lực, nếu kết quả là 1 lá có khả năng gây sát thương cho mục tiêu, bạn có thể thu lấy lá đó;
▷ Bạn có thể lệnh cho người đang có lượt +1 giới hạn sử dụng [Sát] và +1 giới hạn trữ bài.

### Ngụy Đế — `weidi`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người khác đã nhận bài từ chồng bài rút trong lượt này, yêu cầu họ chấp hành 1 [Quân Lệnh], nếu họ không chấp hành, bạn thu lấy toàn bộ bài trên tay họ, sau đó giao cho họ lượng bài tương đương.

### Dong Tứ — `yongsi`

Tỏa định kỹ:
• Nếu không có [Ngọc Tỷ] trong vùng trang bị của tất cả mọi người, bạn xem như có [Ngọc Tỷ].
• Sau khi bạn trở thành mục tiêu của lá [Tri Bỉ Tri Kỷ], bạn mở ra tất cả bài trên tay.

### Phụ Địch — `fudi`

Sau khi bạn nhận sát thương, bạn có thể giao cho nguồn sát thương 1 lá bài trên tay;
▷ Bạn gây 1 sát thương cho 1 người cùng thế lực với nguồn sát thương mà có số máu nhiều nhất trong thế lực đó và ≥ bạn.

### Tòng Gián — `congjian`

Tỏa định kỹ: Khi bạn gây sát thương ngoài lượt hoặc khi bạn tính toán sát thương phải nhận trong lượt, sát thương này +1.

### Kiến Anh — `jianan`

Quân chủ kỹ, Tỏa định kỹ: Bạn có »Ngũ Tử Lương Tướng Đạo«.

»Ngũ Tử Lương Tướng Đạo«: Khi bắt đầu giai đoạn chuẩn bị của người thế lực Ngụy, họ có thể bỏ 1 lá, thực hiện lần lượt:
- Nếu họ đã mở 2 tướng, chọn úp 1 tướng;
- Họ chọn 1 tướng chưa mở của họ, họ không thể mở tướng đã chọn đến khi bắt đầu lượt tiếp theo của họ;
- Họ lựa chọn 1 trong các kỹ năng sau mà chưa có trên bàn: »Đột Kích«, »Kiêu Quả«, »Xảo Biến«, »Tiết Việt«, »Đoạn Lương«, họ nhận kỹ năng đó đến khi bắt đầu lượt tiếp theo của họ.

### Ngũ Tử Lương Tướng Đạo — `elitegeneralflag`

Khi bắt đầu giai đoạn chuẩn bị của người thế lực Ngụy, họ có thể bỏ 1 lá và chọn 1 tướng chưa mở của họ (nếu họ đã mở 2 tướng thì chọn úp 1 tướng);
▷ Họ lựa chọn 1 trong các kỹ năng sau mà chưa có trên bàn: »Đột Kích«, »Kiêu Quả«, »Xảo Biến«, »Tiết Việt«, »Đoạn Lương«, họ nhận kỹ năng đó và không thể mở tướng đã chọn đến khi bắt đầu lượt tiếp theo của họ.

### Huy Tiên — `huibian`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người thế lực Ngụy và 1 người thế lực Ngụy khác đang bị thương, thực hiện lần lượt:
- Bạn gây 1 sát thương cho người đầu tiên và họ rút 2 lá;
- Lệnh người còn lại hồi 1 máu.

### Tổng Ngự — `zongyu`

• Khi [Lục Long Tham Giá] tiến vào vùng trang bị của người khác, nếu có Ngựa trong vùng trang bị của bạn, bạn có thể hoán đổi tất cả Ngựa trong vùng trang bị của bạn với [Lục Long Tham Giá].
• Khi bạn sử dụng 1 lá Ngựa, nếu trên bàn hoặc chồng bài bỏ có [Lục Long Tham Giá], bạn có thể đem [Lục Long Tham Giá] đặt vào vùng trang bị của bạn.

### Lục Long Tham Giá — `SixDragons`

Bài Trang Bị - Ngựa đặc biệt

Kỹ năng: Tỏa định kỹ:
• Khoảng cách từ bạn đến người khác -1.
• Khoảng cách từ người khác đến bạn +1.
• Sau khi [Lục Long Tham Giá] tiến vào vùng trang bị của bạn, bạn bỏ đi tất cả Ngựa khác.
• Lá Ngựa khác không thể tiến vào vùng trang bị của bạn.


## StandardPackage

Nguồn: `lang\vi_VN\Package\StandardPackage.lua`

Tên nhân vật nhận diện được: Bạch Ngân Sư Tử (`SilverLion`).

### Sát — `slash`

Bài cơ bản

Giới hạn: Một lần trong giai đoạn ra bài đối với tất cả loại [Sát]
Lựa chọn: 1 người trong tầm đánh.
Mục tiêu: Người đã chọn
Hiệu quả: Gây 1 sát thương cho mục tiêu.

### Sát Hỏa — `fire_slash`

Bài cơ bản

Giới hạn: Một lần trong giai đoạn ra bài đối với tất cả loại [Sát]
Lựa chọn: 1 người trong tầm đánh.
Mục tiêu: Người đã chọn
Hiệu quả: Gây 1 sát thương Hỏa cho mục tiêu.

### Sát Lôi — `thunder_slash`

Bài cơ bản

Giới hạn: Một lần trong giai đoạn ra bài đối với tất cả loại [Sát]
Lựa chọn: 1 người trong tầm đánh.
Mục tiêu: Người đã chọn
Hiệu quả: Gây 1 sát thương Lôi cho mục tiêu.

### Thiểm — `jink`

Bài cơ bản

Thời điểm: Khi lá [Sát] có hiệu quả với bạn
Hiệu quả: Triệt tiêu hiệu quả của lá[Sát] này với bạn.

### Đào — `peach`

Bài cơ bản

Cách thức I: 
Mục tiêu: Bạn nếu đang bị thương.
Hiệu quả: Mục tiêu hồi 1 máu.

Cách thức II:
Thời điểm: Khi 1 người trong trạng thái hấp hối.
Mục tiêu: Người đang trong trạng thái hấp hối.
Hiệu quả: Mục tiêu hồi 1 máu.

### Tửu — `analeptic`

Bài cơ bản

Cách thức I: 
Giới hạn: Một lần trong lượt của mỗi người.
Mục tiêu: Bạn.
Hiệu quả: Lá [Sát] tiếp theo mục tiêu sử dụng trong lượt này +1 sát thương.

Cách thức II: 
Thời điểm: Khi bạn trong trạng thái hấp hối.
Mục tiêu: Bạn.
Hiệu quả: Mục tiêu hồi 1 máu

### Gia Cát Liên Nỏ — `Crossbow`

Bài trang bị - Vũ khí

Tầm đánh: 1
Kỹ năng: Tỏa định kỹ: bạn không giới hạn số lần sử dụng lá [Sát].

### Thư Hùng Song Cổ Kiếm — `DoubleSword`

Bài trang bị - Vũ khí

Tầm đánh: 2
Kỹ năng: Sau khi xác định từng mục tiêu của [Sát], nếu mục tiêu khác giới tính với bạn, bạn có thể lệnh mục tiêu chọn bỏ 1 lá bài trên tay hoặc lệnh bạn rút 1 lá bài.

### Ngô Lục Kiếm — `SixSwords`

Bài trang bị - Vũ khí

Tầm đánh: 2
Kỹ năng: Tỏa định kỹ: người khác có thế lực giống bạn +1 tầm đánh.

### Tam Tiêm Lưỡng Nhận Đao — `Triblade`

Bài trang bị - Vũ khí

Tầm đánh: 3Kỹ năng: Sau khi bạn gây sát thương cho mục tiêu của lá [Sát], bạn có thể bỏ 1 lá bài trên tay và chọn 1 người khác ở khoảng cách 1 của mục tiêu, bạn gây 1 sát thương cho họ.

### Thanh Công Kiếm — `QinggangSword`

Bài trang bị - Vũ khí

Tầm đánh: 2
Kỹ năng: Tỏa định kỹ: Sau khi bạn xác định mục tiêu của lá [Sát], ứng với mỗi mục tiêu, bạn lệnh [Sát] này Bỏ qua phòng cụ của họ.
Bỏ qua phòng cụ: Vô hiệu hoá phòng cụ người bị bỏ qua phòng cụ đến khi xác định số sát thương cuối cùng mà họ phải nhận.

### Trượng Bát Xà Mâu — `Spear`

Bài trang bị - Vũ khí

Tầm đánh: 3
Kỹ năng: Bạn có thể chuyển hóa sử dụng/đánh ra 2 lá trên tay thành [Sát].

### Quán Thạch Phủ — `Axe`

Bài trang bị - Vũ khí

Tầm đánh: 3
Kỹ năng: Sau khi [Sát] bạn sử dụng bị triệt tiêu bởi [Thiểm] của mục tiêu, bạn có thể bỏ 2 lá, lệnh cho [Sát] này vẫn có hiệu quả đối với mục tiêu này.

### Kỳ Lân Cung — `KylinBow`

Bài trang bị - Vũ khí

Tầm đánh: 5
Kỹ năng: Khi bạn gây sát thương cho mục tiêu của [Sát], bạn có thể bỏ 1 Ngựa trong vùng trang bị của mục tiêu.

### Bát Quái Trận — `EightDiagram`

Bài trang bị - Phòng cụ

Kỹ năng: Khi bạn được yêu cầu sử dụng/đánh ra [Thiểm], bạn có thể tiến hành Phán xét, nếu kết quả phán xét có màu Đỏ, xem như bạn đã sử dụng/đánh ra [Thiểm].

### Nhân Vương Thuẫn — `RenwangShield`

Bài trang bị - Phòng cụ

Kỹ năng: Tỏa định kỹ: [Sát] Đen không có hiệu quả với bạn.

### Hàn Băng Kiếm — `IceSword`

Bài trang bị - Vũ khí

Tầm đánh: 2
Kỹ năng: Khi bạn gây sát thương cho mục tiêu của [Sát], nếu mục tiêu có bài, bạn có thể chặn sát thương này và lần lượt bỏ 2 lá của mục tiêu.

### Chu Tước Vũ Phiến — `Fan`

Bài trang bị - Vũ khí

Tầm đánh: 4
Kỹ năng: Khi bạn sử dụng [Sát] phổ thông, bạn có thể chuyển hóa [Sát] này thành [Sát Hỏa].

### Bạch Ngân Sư Tử — `SilverLion`

Bài trang bị - Phòng cụ

Kỹ năng: Tỏa định kỹ:
• Khi bạn nhận sát thương, nếu sát thương này > 1, sát thương này trở thành 1.
• Sau khi bạn mất [Bạch Ngân Sư Tử] từ vùng trang bị của bạn, bạn hồi 1 máu.

### Đằng Giáp — `Vine`

Bài trang bị - Phòng cụ

Kỹ năng: Tỏa định kỹ:
• [Nam Man Nhập Xâm], [Vạn Tiễn Tề Phát] và [Sát] phổ thông không có hiệu quả với bạn.
• Khi bạn tính toán sát thương phải nhận, nếu sát thương này có thuộc tính Hỏa, sát thương này +1.

### +1 horse — `+1 horse`

Bài trang bị - Ngựa +1

Kỹ năng: Tỏa định kỹ: khoảng cách từ người khác đến bạn +1.

### -1 horse — `-1 horse`

Bài trang bị - Ngựa -1

Kỹ năng: Tỏa định kỹ: khoảng cách từ bạn đến người khác -1.

### Ngũ Cốc Phong Đăng — `amazing_grace`

Bài công cụ

Mục tiêu: Tất cả
Hiệu quả: Lật ra từ chồng bài số lá bài bằng với số mục tiêu; mục tiêu thu lấy 1 lá từ số bài đã lật ra.

### Đào Viên Kết Nghĩa — `god_salvation`

Bài Công cụ

Mục tiêu: Tất cả
Hiệu quả: Mục tiêu hồi 1 máu; Không có hiệu quả với mục tiêu không bị thương.

### Nam Man Nhập Xâm — `savage_assault`

Bài công cụ

Mục tiêu: Tất cả người khác
Hiệu quả: Mục tiêu cần đánh ra 1 lá [Sát]; nếu không, họ nhận 1 sát thương.

### Vạn Tiễn Tề Phát — `archery_attack`

Bài công cụ

Mục tiêu: Tất cả người khác.
Hiệu quả: Mục tiêu cần đánh ra 1 lá [Thiểm]; nếu không, họ nhận 1 sát thương.

### Tá Đao Sát Nhân — `collateral`

Bài công cụ

Lựa chọn: 1 người khác có vũ khí trong vùng trang bị (gọi là A) và 1 người trong tầm đánh của A (gọi là B)
Mục tiêu: A
Hiệu quả: A cần sử dụng [Sát] với B, nếu không, họ giao vũ khí trong vùng trang bị cho bạn.

### Quyết Đấu — `duel`

Bài công cụ

Lựa chọn: 1 người khác
Mục tiêu: Người đã chọn.
Hiệu quả: Bắt đầu từ mục tiêu và bạn lần lượt đánh ra lá [Sát] đến khi có người  không đánh ra lá[Sát], người đó nhận 1 sát thương từ người còn lại.

### Vô Trung Sinh Hữu — `ex_nihilo`

Bài công cụ

Mục tiêu: Bạn
Hiệu quả: Mục tiêu rút 2 lá.

### Thuận Thủ Khiên Dương — `snatch`

Bài công cụ

Lựa chọn: 1 người khác ở khoảng cách 1 của bạn và có bài trong vùng chơi
Mục tiêu: Người đã chọn
Hiệu quả: Bạn thu lấy 1 lá trong vùng chơi của mục tiêu.

### Quá Hạ Sách Kiều — `dismantlement`

Bài công cụ

Lựa chọn: 1 người khác có bài trong vùng chơi
Mục tiêu: Người đã chọn.
Hiệu quả: Bạn bỏ 1 lá trong vùng chơi của mục tiêu.

### Vô Giải Khả Kích — `nullification`

Bài công cụ

Thời điểm: Khi 1 lá công cụ có hiệu quả với 1 người hoặc khi [Vô Giải Khả Kích] có hiệu quả.
Hiệu quả: Triệt tiêu hiệu quả của lá công cụ với người đó; hoặc triệt tiêu hiệu quả của [Vô Giải Khả Kích];
▷ Nếu công cụ bị triệt tiêu là [Thiểm Điện], chuyển lá đó sang người tiếp theo.

### Vô Giải Khả Kích - Quốc — `heg_nullification`

Bài công cụ

Thời điểm: Khi 1 lá công cụ có hiệu quả với 1 người hoặc khi [Vô Giải Khả Kích] có hiệu quả.
Hiệu quả: Triệt tiêu hiệu quả của lá công cụ với người đó hoặc tất cả người cùng thế lực với người đó; hoặc triệt tiêu hiệu quả của [Vô Giải Khả Kích];
▷ Nếu công cụ bị triệt tiêu là [Thiểm Điện], chuyển lá đó sang người tiếp theo.

### Lạc Bất Tư Thục — `indulgence`

Bài công cụ thời gian

Lựa chọn: 1 người khác
Mục tiêu: Người đã chọn
Hiệu quả: Giai đoạn phán xét của mục tiêu, họ tiến hành phán xét, nếu kết quả phán xét không phải chất CƠ, bỏ qua giai đoạn ra bài lượt này; sau đó đưa lá này vào chồng bài bỏ.

### Thiểm Điện — `lightning`

Bài công cụ thời gian

Mục tiêu: Bạn
Hiệu quả: Giai đoạn phán xét của mục tiêu, tiến hành phán xét, nếu kết quả phán xét từ 2~9 BÍCH, mục tiêu nhận 3 điểm sát thương Lôi, sau đó đưa lá này vào chồng bài bỏ; nếu không, lá [Thiểm Điện] chuyển sang người tiếp theo.

### Thiết Tác Liên Hoàn — `iron_chain`

Bài công cụ

Lựa chọn: 1-2 người
Mục tiêu: Người đã chọn
Hiệu quả: Mục tiêu thay đổi trạng thái xích.
Trùng Chú: Có thể đưa lá này vào chồng bài bỏ để rút 1 lá.

### Hỏa Công — `fire_attack`

Bài công cụ

Lựa chọn: 1 người có bài trên tay
Mục tiêu: Người đã chọn.
Hiệu quả: Mục tiêu mở 1 lá trên tay, bạn có thể bỏ 1 lá trên tay có cùng chất với lá họ đã mở để gây 1 sát thương Hỏa cho mục tiêu.

### Binh Lương Thốn Đoạn — `supply_shortage`

Bài công cụ thời gian

Lựa chọn: 1 người khác ở khoảng cách 1
Mục tiêu: Người đã chọn
Hiệu quả: Giai đoạn phán xét của mục tiêu, họ tiến hành phán xét, nếu kết quả phán xét không phải chất TÉP, bỏ qua giai đoạn rút bài lượt này; sau đó đưa lá này vào chồng bài bỏ.

### Dĩ Dật Đãi Lao — `await_exhausted`

Bài công cụ

Mục tiêu: Tất cả người có cùng thế lực với bạn.
Hiệu quả: Mục tiêu rút 2 lá và bỏ 2 lá.

### Tri Bỉ Tri Kỉ — `known_both`

Bài công cụ

Lựa chọn: 1 người khác có tướng chưa mở hoặc có bài trên tay
Mục tiêu: Người đã chọn
Hiệu quả: Bạn chọn xem tất cả bài trên tay hoặc 1 tướng úp của mục tiêu.
Trùng Chú: Có thể đưa lá này vào chồng bài bỏ để rút 1 lá.

### Viễn Giao Cận Công — `befriend_attacking`

Bài công cụ

Lựa chọn: 1 người có thế lực xác định khác bạn
Mục tiêu: Người đã chọn
Hiệu quả: Mục tiêu rút 1 lá, sau đó bạn rút 3 lá.

## StandardQunGeneral

Nguồn: `lang\vi_VN\Package\StandardQunGeneral.lua`

Tên nhân vật nhận diện được: Hoa Đà (`huatuo`); Lữ Bố (`lvbu`); Điêu Thuyền (`diaochan`); Viên Thiệu (`yuanshao`); Nhan Lương & Văn Xú (`yanliangwenchou`); Song Hùng (`shuangxiong`); Giả Hủ (`jiaxu`); Bàng Đức (`pangde`); Trương Giác (`zhangjiao`); Thái Văn Cơ (`caiwenji`); Mã Đằng (`mateng`); Khổng Dung (`kongrong`); Lễ Nhượng (`lirang`); Kỷ Linh (`jiling`); Điền Phong (`tianfeng`); Phan Phụng (`panfeng`); Trâu Thị (`zoushi`).

### Trừ Lệ — `chuli`

Một lần trong giai đoạn ra bài, nếu bạn có bài, bạn có thể chọn tối đa 3 người có thế lực khác nhau và có bài, thực hiện lần lượt:
- Bạn bỏ đi 1 lá của bạn và họ;
- Lệnh người đã mất đi lá BÍCH bởi kỹ năng này rút 1 lá.

### Cấp Cứu — `jijiu`

Ngoài lượt của bạn, bạn có thể chuyển hóa sử dụng bài Đỏ thành [Đào].

### Vô Song — `wushuang`

Tỏa định kỹ:
• Sau khi bạn xác định mục tiêu của [Sát], ứng với mỗi mục tiêu, bạn lệnh họ cần sử dụng 2 [Thiểm] để triệt tiêu [Sát] này.
• Sau khi bạn xác định mục tiêu của [Quyết Đấu] ứng với mỗi mục tiêu hoặc sau khi bạn trở thành mục tiêu của [Quyết Đấu], bạn lệnh người cùng bạn [Quyết Đấu] cần đánh ra 2 [Sát] mỗi lần để hưởng ứng.
• Sau khi bạn lựa chọn mục tiêu cho [Quyết Đấu] phi chuyển hóa, bạn có thể lựa chọn thêm tối đa 2 người để trở thành mục tiêu.

### Ly Gián — `lijian`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 1 lá và lựa chọn 2 người khác có giới tính nam, lệnh người chọn sau xem như sử dụng [Quyết Đấu] với người chọn trước.

### Bế Nguyệt — `biyue`

Khi bắt đầu giai đoạn kết thúc, bạn có thể rút 1 lá.

### Loạn Kích — `luanji`

Giai đoạn ra bài, bạn có thể chuyển hóa sử dụng 2 lá trên tay thành [Vạn Tiễn Tề Phát];
▷ Bạn không thể sử dụng [Vạn Tiễn Tề Phát] bằng cách này với lá thành phần cùng chất với những lá bạn đã sử dụng theo cách này trong lượt này;
▶ Sau khi người cùng thế lực với bạn đánh ra [Thiểm] để hưởng ứng, họ có thể rút 1 lá.

### Song Hùng — `shuangxiong`

Giai đoạn rút bài, bạn có thể chọn không rút bài, bạn tiến hành phán xét;
▶ Sau khi phán xét trên có hiệu lực, bạn thu lấy kết quả phán xét;
▶ Trong lượt này, bạn có thể chuyển hóa sử dụng bài trên tay khác màu với kết quả phán xét trên thành [Quyết Đấu].

### Hoàn Sát — `wansha`

Tỏa định kỹ: Trong lượt của bạn, khi có người vào trạng thái hấp hối, bạn lệnh người khác không trong trạng thái hấp hối không thể sử dụng [Đào].

### Duy Mạc — `weimu`

Tỏa định kỹ:
• Khi bạn trở thành mục tiêu của công cụ phổ thông Đen, hủy bỏ mục tiêu đối với bạn.
• Khi có lá Đen tiến vào vùng phán xét của bạn, đưa lá đó vào chồng bài bỏ.

### Loạn Vũ — `luanwu`

Hạn định kỹ: Giai đoạn ra bài, bạn có thể phát động kỹ năng này, lệnh tất cả người khác chọn 1 mục:
1. Họ sử dụng [Sát] với người có khoảng cách nhỏ nhất;
2. Họ mất 1 máu.

### Kiện Xuất — `jianchu`

Sau khi bạn xác định mục tiêu của [Sát], ứng với mỗi mục tiêu, bạn có thể bỏ 1 lá của họ, nếu lá bị bỏ đi là:
* Trang bị: Họ không thể sử dụng [Thiểm] để hưởng ứng;
* Phi trang bị: Họ thu lấy [Sát] mà bạn sử dụng.

### Lôi Kích — `leiji`

Khi bạn sử dụng/đánh ra [Thiểm], bạn có thể lệnh 1 người khác tiến hành phán xét, nếu kết quả phán xét có chất BÍCH, bạn gây 2 sát thương Lôi cho họ.

### Quỷ Đạo — `guidao`

Khi phán xét của 1 người có hiệu lực, bạn có thể đánh ra 1 lá Đen để hoán đổi kết quả phán xét đó.

### Bi ca — `beige`

Sau khi 1 người nhận sát thương từ lá [Sát], bạn có thể bỏ 1 lá, lệnh họ tiến hành phán xét, nếu kết quả phán xét có chất:
* CƠ: Họ hồi 1 máu;
* RÔ: Họ rút 2 lá;
* TÉP: Nguồn sát thương bỏ 2 lá;
* BÍCH: Nguồn sát thương thay đổi trạng thái chồng tướng.

### Đoạn Trường — `duanchang`

Tỏa định kỹ: Khi bạn trận vong do người khác gây sát thương, bạn chọn 1 tướng của họ, lệnh họ mất đi kỹ năng của tướng đó.

### Hùng Dị — `xiongyi`

Hạn định kỹ: Giai đoạn ra bài, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Lệnh tất cả người cùng thế lực với bạn rút 3 lá;
- Nếu thế lực của bạn là một trong những thế lực ít người nhất, bạn hồi 1 máu.

### Danh Sĩ — `mingshi`

Tỏa định kỹ: Khi bạn tính toán sát thương phải nhận, nếu nguồn sát thương có tướng chưa mở, lệnh sát thương này -1.

### Lễ Nhượng — `lirang`

Khi bài của bạn tiến vào chồng bài bỏ do bỏ bài, bạn có thể giao tùy ý cho những người khác.

### Song Nhận — `shuangren`

Khi bắt đầu giai đoạn ra bài, bạn có thể đấu điểm với 1 người:
* Nếu bạn thắng: Bạn xem như sử dụng [Sát] với 1 người cùng thế lực với họ;
* Nếu bạn không thắng: Bạn không thể chỉ định người khác làm mục tiêu sử dụng bài.

### Tử Gián — `sijian`

Sau khi bạn mất đi lá cuối cùng trên tay, bạn có thể bỏ 1 lá của 1 người khác.

### Tùy Thế — `suishi`

Tỏa định kỹ:
• Khi người khác tiến trạng thái hấp hồi, nếu nguồn sát thương có cùng thế lực với bạn, bạn rút 1 lá.
• Khi người khác có cùng thế lực với bạn trận vong, bạn mất 1 máu.

### Cuồng Phủ — `kuangfu`

Một lần trong giai đoạn ra bài, sau khi bạn xác định mục tiêu của [Sát], bạn có thể thu lấy 1 trang bị của 1 trong các mục tiêu;
▶ Sau khi kết toán xong [Sát] này, nếu [Sát] này không gây sát thương, bạn bỏ 2 lá trên tay.

### Họa Thủy — `huoshui`

Tỏa định kỹ: Trong lượt của bạn:
• Người khác không thể mở tướng.
• Khi bạn sử dụng [Sát] hoặc [Vạn Tiễn Tề Phát], mục tiêu của lá này không thể sử dụng hoặc đánh ra [Thiểm] để hưởng ứng.

### Khuynh Thành — `qingcheng`

Giai đoạn ra bài, bạn có thể bỏ 1 lá Đen và chọn 1 người khác đã mở tất cả tướng, bạn úp 1 tướng của họ;
▷ Nếu lá bạn bỏ là trang bị, bạn có thể chọn 1 người khác đã mở tất cả tướng, bạn úp 1 tướng của họ.

## StandardShuGeneral

Nguồn: `lang\vi_VN\Package\StandardShuGeneral.lua`

Tên nhân vật nhận diện được: Lưu Bị (`liubei`); Quan Vũ (`guanyu`); Trương Phi (`zhangfei`); Gia Cát Lượng (`zhugeliang`); Triệu Vân (`zhaoyun`); Mã Siêu (`machao`); Hoàng Nguyệt Anh (`huangyueying`); Hoàng Trung (`huangzhong`); Ngụy Diên (`weiyan`); Bàng Thống (`pangtong`); Khổng Minh (`wolong`); Lưu Thiện (`liushan`); Mạnh Hoạch (`menghuo`); Chúc Dung (`zhurong`); Cam Phu Nhân (`ganfuren`).

### Nhân Đức — `rende`

Giai đoạn ra bài, bạn có thể đem tùy ý lượng bài trên tay giao cho 1 người khác chưa nhận bài từ kỹ năng này trong giai đoạn này;
▷ Nếu đây là lần đầu tổng số lá bạn giao bằng kỹ năng này trong giai đoạn này ≥ 2, bạn có thể xem như sử dụng 1 lá cơ bản.

### Võ Thánh — `wusheng`

• Bạn có thể chuyển hóa sử dụng/đánh ra 1 lá Đỏ thành [Sát].
• Lá [Sát] RÔ do bạn sử dụng không giới hạn khoảng cách.

### Bào Hao — `paoxiao`

Tỏa định kỹ:
• Bạn sử dụng lá [Sát] không giới hạn số lượng.
• Khi bạn sử dụng [Sát] thứ 2 trong 1 lượt, bạn rút 1 lá.

### Quan Tinh — `guanxing`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể xem X lá bài trên đầu chồng bài rút (X là số người còn sống, tối đa 5), sau đó sắp xếp tùy ý những lá này lên đầu hoặc đáy chồng bài rút.

### Không Thành — `kongcheng`

Tỏa định kỹ:
• Khi bạn trở thành mục tiêu của [Sát]/[Quyết Đấu], nếu bạn không có bài trên tay, hủy bỏ mục tiêu đối với bạn.
• Ngoài lượt của bạn, khi bạn nhận được bài do người khác giao cho, nếu bạn không có bài trên tay, đặt những lá bài này lên trên Tướng này, gọi là [Cầm];
• Khi bắt đầu giai đoạn rút bài, bạn thu lấy tất cả lá [Cầm].

### Long Đảm — `longdan`

• Bạn có thể chuyển hóa sử dụng/đánh ra [Thiểm] thành [Sát];
▶ Sau khi [Sát] này bị triệt tiêu bởi [Thiểm] của mục tiêu, bạn có thể gây 1 sát thương cho 1 người ngoại trừ mục tiêu.
• Bạn có thể chuyển hóa sử dụng/đánh ra [Sát] thành [Thiểm];
▶ Sau khi [Thiểm] này triệt tiêu [Sát] của 1 người, bạn có thể hồi 1 máu cho 1 người khác ngoại trừ người sử dụng [Sát].

### mashu — `mashu`

Tỏa định kỹ: Khoảng cách từ bạn đến người khác -1.

### Thiết Kỵ — `tieqi`

Sau khi bạn xác định mục tiêu của [Sát], ứng với mỗi mục tiêu, bạn có thể tiến hành phán xét, thực hiện lần lượt:
- Vô hiệu hóa kỹ năng không phải Tỏa định kỹ của 1 tướng đã mở của mục tiêu trong lượt này;
- Mục tiêu chọn bỏ 1 lá cùng chất với kết quả phán xét hoặc không thể sử dụng [Thiểm] để hưởng ứng [Sát] này.

### Tập Trí — `jizhi`

Khi bạn sử dụng công cụ phổ thông không phải chuyển hóa, bạn có thể rút 1 lá.

### Kỳ Tài — `qicai`

Tỏa định kỹ: Công cụ bạn sử dụng không giới hạn khoảng cách.

### Liệt Cung — `liegong`

• Lá [Sát] bạn sử dụng không giới hạn khoảng cách với mục tiêu có số bài trên tay ≤ bạn.
• Sau khi bạn xác định từng mục tiêu của [Sát], nếu số máu của họ ≥ bạn, bạn có thể chọn 1 mục:
1. Lệnh mục tiêu không thể sử dụng [Thiểm] để hưởng ứng [Sát] này;
2. Lệnh cho sát thương từ hiệu quả của lá [Sát] này +1 đối với mục tiêu này.

### Cuồng Cốt — `kuanggu`

Sau khi bạn gây sát thương cho 1 người, nếu khoảng cách từ bạn tới họ ≤1 trước khi máu giảm, ứng với mỗi sát thương, bạn có thể chọn 1 mục:
1. Hồi 1 máu;
2. Rút 1 lá.

### Liên Hoàn — `lianhuan`

Giai đoạn ra bài, bạn có thể chuyển hóa sử dụng lá TÉP trên tay thành [Thiết Tác Liên Hoàn] hoặc Trùng Chú lá TÉP trên tay.

### Niết Bàn — `niepan`

Hạn định kỹ: Khi bạn trong trạng thái hấp hối, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Bạn bỏ toàn bộ bài trong vùng chơi;
- Bạn hồi máu đến 3 và rút 3 lá;
- Bạn loại bỏ trạng thái xích và chồng tướng.

### Bát Trận — `bazhen`

Tỏa định kỹ: Nếu vùng trang bị của bạn không có phòng cụ, bạn xem như có [Bát Quái Trận].

### Hỏa Kế — `huoji`

Bạn có thể chuyển hóa sử dụng lá Đỏ trên tay thành [Hỏa Công].

### Khán Phá — `kanpo`

Bạn có thể chuyển hóa sử dụng lá Đen trên tay thành [Vô Giải Khả Kích].

### Hưởng Lạc — `xiangle`

Tỏa định kỹ: Sau khi bạn trở thành mục tiêu của [Sát], người sử dụng [Sát] chọn 1 mục:
1. Họ bỏ 1 lá cơ bản;
2. Lệnh [Sát] đó không có hiệu quả với bạn.

### Ủy Quyền — `fangquan`

Khi tiến vào giai đoạn ra bài, bạn có thể bỏ qua giai đoạn này;
▶ Khi kết thúc lượt này, bạn có thể bỏ 1 lá bài trên tay, lệnh 1 người có 1 lượt sau lượt này.

### Họa Thủ — `huoshou`

Tỏa định kỹ:
• [Nam Man Nhập Xâm] không có hiệu quả với bạn.
• Sau khi 1 người khác xác định mục tiêu của [Nam Man Nhập Xâm], bạn trở thành nguồn sát thương của [Nam Man Nhập Xâm] này.

### Tái Khởi — `zaiqi`

Khi kết thúc giai đoạn bỏ bài, bạn có thể chọn tối đa X người cùng thế lực (X là số lá Đỏ đã đi vào chồng bài bỏ trong lượt này), họ lựa chọn 1 mục:
1. Họ rút 1 lá;
2. Lệnh bạn hồi 1 máu.

### Cự Tượng — `juxiang`

Tỏa định kỹ:
• [Nam Man Nhập Xâm] không có hiệu quả với bạn.
• Sau khi [Nam Man Nhập Xâm] do người khác sử dụng kết toán xong, bạn thu lấy lá này.

### Liệt Nhận — `lieren`

Sau khi bạn gây sát thương cho mục tiêu của [Sát], bạn có thể tiến hành đấu điểm với họ, nếu bạn thắng, bạn thu lấy 1 lá của mục tiêu.

### Thục Thận — `shushen`

Sau khi bạn hồi máu, ứng với mỗi máu bạn đã hồi, bạn có thể lệnh 1 người khác rút 1 lá.

### Thần Trí — `shenzhi`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể bỏ tất cả bài trên tay, nếu số lá đã bỏ ≥ số máu hiện tại của bạn, bạn hồi 1 máu.

## StandardWeiGeneral

Nguồn: `lang\vi_VN\Package\StandardWeiGeneral.lua`

Tên nhân vật nhận diện được: Tào Tháo (`caocao`); Tư Mã Ý (`simayi`); Hạ Hầu Đôn (`xiahoudun`); Trương Liêu (`zhangliao`); Hứa Chử (`xuchu`); Quách Gia (`guojia`); Di Kế (`yiji`); Chân Cơ (`zhenji`); Hạ Hầu Uyên (`xiahouyuan`); Trương Cáp (`zhanghe`); Xảo Biến (`qiaobian`); Từ Hoảng (`xuhuang`); Tào Nhân (`caoren`); Điển Vi (`dianwei`); Tuân Úc (`xunyu`); Tào Phi (`caopi`); Nhạc Tiến (`yuejin`).

### Gian Hùng — `jianxiong`

Sau khi bạn nhận sát thương, bạn có thể thu lấy lá gây sát thương cho bạn.

### Phản Quỹ — `fankui`

Sau khi bạn nhận sát thương, bạn có thể thu lấy 1 lá của nguồn sát thương.

### Quỷ Tài — `guicai`

Khi phán xét của 1 người có hiệu lực, bạn có thể đánh ra 1 lá để thay thế kết quả phán xét đó.

### Cương Liệt — `ganglie`

Sau khi bạn nhận sát thương, bạn có thể tiến hành phán xét, nếu màu của kết quả phán xét có màu:
* Đỏ: Bạn gây 1 sát thương cho nguồn sát thương;
* Đen: bạn bỏ 1 lá của nguồn sát thương

### Tập Kích — `tuxi`

Giai đoạn rút bài, bạn có thể chọn rút bớt X lá và chọn X người khác có bài trên tay, thu lấy 1 lá trên tay của mỗi người.

### Lỏa Y — `luoyi`

Khi kết thúc giai đoạn rút bài, bạn có thể bỏ 1 lá;
▶ Trong lượt này, khi bạn gây sát thương cho mục tiêu của [Sát] hoặc [Quyết Đấu], sát thương này +1.

### Thiên Khiển — `tiandu`

Sau khi phán xét của bạn có hiệu lực, bạn có thể thu lấy kết quả phán xét.

### Di Kế — `yiji`

Sau khi bạn nhận sát thương, bạn có thể xem 2 lá bài trên đầu chồng bài rút và giao cho tùy ý người.

### Lạc Thần — `luoshen`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể phát động kỹ năng này, thực hiện lần lượt:
- Bạn tiến hành phán Xét, nếu kết quả phán xét có màu Đen, bạn có thể lặp lại quá trình này;
- Bạn thu lấy tất cả kết quả phán xét có màu Đen.

### Khuynh Quốc — `qingguo`

Bạn có thể chuyển hóa sử dụng/đánh ra lá Đen trên tay thành [Thiểm].

### Thần Tốc — `shensu`

Nếu bạn thỏa mãn điều kiện sử dụng [Sát] (bỏ qua giới hạn khoảng cách), khi bạn tiến vào giai đoạn:
* Phán xét: Bạn có thể bỏ qua giai đoạn này và giai đoạn rút bài;
* Ra bài: Bạn có thể bỏ qua giai đoạn này và bỏ 1 lá trang bị;
* Bỏ bài: Bạn có thể bỏ qua giai đoạn này và mất 1 máu;
▷ Bạn xem như sử dụng [Sát] không giới hạn khoảng cách.

### Xảo Biến — `qiaobian`

Khi tiến vào 1 giai đoạn trong lượt của bạn (Ngoại trừ giai đoạn chuẩn bị và kết thúc), bạn có thể bỏ 1 lá bài trên tay để bỏ qua giai đoạn này; sau đó nếu giai đoạn đã bỏ qua là:
* Rút bài: Bạn có thể chọn tối đa 2 người có bài trên tay, bạn thu lấy 1 lá trên tay mỗi người;
* Ra bài: Bạn có thể di chuyển 1 lá trên bàn chơi.

### Đoạn Lương — `duanliang`

Bạn có thể chuyển hóa sử dụng lá Đen không phải Công cụ thành [Binh Lương Thốn Đoạn] không giới hạn khoảng cách;
▷ Nếu khoảng cách giữa bạn và mục tiêu > 2, bạn không thể phát động kỹ năng này trong giai đoạn này.

### Chiếm Thủ — `jushou`

Khi bắt đầu giai đoạn kết thúc, bạn có thể rút X lá (X là số thế lực còn sống), thực hiện lần lượt:
- Bạn sử dụng 1 trang bị trên tay hoặc bỏ 1 lá phi trang bị;
- Nếu bạn rút > 2 lá, bạn thay đổi trạng thái chồng tướng.

### Cường Kích — `qiangxi`

Một lần trong giai đoạn ra bài, bạn có thể chọn 1 người khác, bạn chọn bỏ 1 Vũ khí hoặc mất 1 máu, bạn gây 1 sát thương cho họ.

### Vờn Hổ — `quhu`

Một lần trong giai đoạn ra bài, bạn có thể tiến hành đấu điểm với 1 người có số máu > bạn:
* Nếu bạn thắng: Họ gây 1 sát thương cho 1 người trong tầm đánh của họ do bạn chỉ định;
* Nếu bạn không thắng: Họ gây 1 sát thương cho bạn.

### Tiết Mệnh — `jieming`

Sau khi bạn nhận sát thương, bạn có thể chọn 1 người, lệnh họ bổ sung bài trên tay đến giới hạn máu (Tối đa 5).

### Hành Thương — `xingshang`

Khi 1 người khác trận vong, bạn có thể thu lấy tất cả bài của họ.

### Lưu Đày — `fangzhu`

Sau khi bạn nhận sát thương, bạn có thể lệnh 1 người khác lựa chọn 1 mục:
1. Họ rút X lá, sau đó thay đổi trạng thái chồng tướng;
2. Họ bỏ X lá, sau đó mất 1 máu;
(X là số máu đã mất của bạn).

### Dũng Mãnh — `xiaoguo`

Khi bắt đầu giai đoạn kết thúc của 1 người khác, bạn có thể bỏ 1 lá cơ bản, lệnh họ chọn 1 mục:
1. Họ bỏ 1 trang bị và lệnh bạn rút 1 lá;
2. Bạn gây 1 sát thương cho họ.

## StandardWuGeneral

Nguồn: `lang\vi_VN\Package\StandardWuGeneral.lua`

Tên nhân vật nhận diện được: Tôn Quyền (`sunquan`); Cam Ninh (`ganning`); Lữ Mông (`lvmeng`); Hoàng Cái (`huanggai`); Chu Du (`zhouyu`); Đại Kiều (`daqiao`); Lục Tốn (`luxun`); Tôn Thượng Hương (`sunshangxiang`); Tôn Kiên (`sunjian`); Anh Hồn (`yinghun_sunjian`); Tiểu Kiều (`xiaoqiao`); Thái Sử Từ (`taishici`); Chu Thái (`zhoutai`); Lỗ Túc (`lusu`); Trương Chiêu & Trương Hoành (`erzhang`); Cổ Chính (`guzheng`); Đinh Phụng (`dingfeng`).

### Chế Hành — `zhiheng`

Một lần trong giai đoạn ra bài, bạn có thể bỏ tối đa X lá (X là giới hạn máu của bạn), bạn rút số lá tương ứng.

### Kỳ Tập — `qixi`

Giai đoạn ra bài, bạn có thể chuyển hóa sử dụng lá Đen thành [Quá Hạ Sách Kiều].

### Khắc Kỷ — `keji`

Tỏa định kỹ: Khi bắt đầu giai đoạn bỏ bài, nếu bạn trong giai đoạn ra bài không sử dụng các lá bài khác màu với nhau, giới hạn trữ bài của bạn trong lượt này +4.

### Mưu Đoạn — `mouduan`

Khi bắt đầu giai đoạn kết thúc, nếu trong giai đoạn ra bài của lượt này bạn đã sử dụng bài từ 4 chất khác nhau hoặc 3 loại bài khác nhau, bạn có thể di chuyển 1 lá trên bàn chơi.

### Khổ Nhục — `kurou`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 1 lá, thực hiện lần lượt:
- Bạn mất 1 máu;
- Bạn rút 3 lá;
- Giới hạn sử dụng [Sát] của bạn trong giai đoạn này +1.

### yingzi — `yingzi`

Tỏa định kỹ:
• Giai đoạn rút bài, bạn rút thêm 1 lá.
• Giới hạn trữ bài của bạn bằng với giới hạn máu.

### Phản Gián — `fanjian`

Một lần trong giai đoạn ra bài, bạn có thể mở ra 1 lá bài trên tay và giao cho 1 người khác, bạn lệnh cho họ lựa chọn 1 mục:
1. Nếu họ có bài trên tay hoặc có lá cùng chất với lá bạn đã mở trong vùng trang bị, họ mở ra tất cả bài trên tay và bỏ đi tất cả lá của họ có cùng chất với lá bạn đã mở ra;
2. Họ mất 1 máu.

### Quốc Sắc — `guose`

Giai đoạn ra bài, bạn có thể chuyển hóa sử dụng lá RÔ thành [Lạc Bất Tư Thục]

### Lưu Ly — `liuli`

Khi bạn trở thành mục tiêu của [Sát], bạn có thể bỏ đi 1 lá, thay đổi mục tiêu của [Sát] này thành người khác trong tầm đánh của bạn (Không thể là người sử dụng [Sát] và người đã là mục tiêu của [Sát] này).

### Khiêm Tốn — `qianxun`

Tỏa định kỹ:
• Khi bạn trở thành mục tiêu của [Thuận Thủ Khiên Dương], hủy bỏ mục tiêu đối với bạn.
• Khi [Lạc Bất Tư Thục] tiến vào vùng phán xét của bạn, đưa lá đó vào chồng bài bỏ.

### Độ Thế — `duoshi`

Bốn lần trong giai đoạn ra bài, bạn có thể chuyển hóa sử dụng bài Đỏ trên tay thành [Dĩ Dật Đãi Lao].

### Kết Nhân — `jieyin`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 2 lá trên tay và chọn 1 người có giới tính nam đang bị thương, bạn và họ hồi 1 máu.

### Kiêu Cơ — `xiaoji`

Sau khi bạn mất bài trong vùng trang bị, bạn có thể:
* Nếu đang là lượt của bạn, bạn rút 1 lá;
* Nếu không phải lượt của bạn, bạn rút 3 lá.

### yinghun — `yinghun`

Khi bắt đầu giai đoạn chuẩn bị, bạn có thể chọn 1 người khác và chọn 1 mục:
1. Lệnh họ rút X lá sau đó bỏ 1 lá;
2. Lệnh họ rút 1 lá sau đó bỏ X lá (X là số máu bạn đã mất).

### Hồng Nhan — `hongyan`

Toả định kỹ:
• Lá BÍCH của bạn và kết quả phán xét BÍCH của bạn xem như CƠ;
• Nếu bạn có lá CƠ trong vùng trang bị, giới hạn trữ bài của bạn +1

### Thiên Hương — `tianxiang`

Hai lần trong lượt của mỗi người, khi bạn nhận sát thương, bạn có thể bỏ 1 lá CƠ trên tay và lựa chọn 1 người khác, bạn chặn sát thương này, sau đó bạn chọn 1 mục mà chưa chọn trong lượt này:
1. Nếu sát thương này có nguồn, bạn lệnh nguồn sát thương gây 1 sát thương cho họ, sau đó họ rút X lá (X là số máu họ đã mất, tối đa 5);
2. Lệnh họ mất 1 máu, sau đó họ thu lấy lá bạn vừa bỏ.

### Thiên Nghĩa — `tianyi`

Một lần trong giai đoạn ra bài, bạn có thể đấu điểm với 1 người:
* Nếu bạn thắng: Trong lượt này, bạn sử dụng [Sát] không giới hạn khoảng cách; giới hạn sử dụng [Sát] và số mục tiêu của [Sát] +1;
* Nếu bạn không thắng: Bạn không thể sử dụng [Sát] trong lượt này.

### Bất Khuất — `buqu`

Tỏa định kỹ: Khi bạn trong trạng thái hấp hối, bạn mở 1 lá trên đầu chồng bài rút và đặt lên tướng này, gọi là [Sang], nếu [Sang] mới đặt so với những [Sang] khác:
* Khác điểm: Bạn hồi máu đến 1;
* Cùng điểm: Bạn đưa [Sang] này vào chồng bài bỏ.

### Phấn Kích — `fenji`

Khi bắt đầu giai đoạn kết thúc của 1 người, nếu họ không có bài trên tay, bạn có thể lệnh cho họ rút 2 lá, sau đó bạn mất 1 máu.

### Hảo Thi — `haoshi`

Giai đoạn rút bài, bạn có thể rút thêm 2 lá;
▶ Sau khi bạn rút bài, nếu số bài trên tay bạn > 5, bạn giao một nửa bài trên tay (làm tròn xuống) cho 1 người khác có số bài trên tay ít nhất.

### Kết Minh — `dimeng`

Một lần trong giai đoạn ra bài, bạn có thể chọn 2 người khác và bỏ đi X lá (X là số bài chênh lệch trên tay giữa 2 người), lệnh họ hoán đổi bài trên tay.

### Trực Gián — `zhijian`

Giai đoạn ra bài, bạn có thể đặt 1 trang bị trên tay vào vùng trang bị trống tương ứng của người khác, sau đó bạn rút 1 lá.

### Cổ Chính — `guzheng`

Khi kết thúc giai đoạn bỏ bài của người khác, bạn có thể giao cho họ 1 lá trong những lá đã bỏ đi trong giai đoạn này;
▷ Bạn có thể thu lấy những lá còn lại.

### Đoản Binh — `duanbing`

Sau khi bạn chỉ định mục tiêu cho [Sát], bạn có thể chỉ định thêm 1 mục tiêu ở khoảng cách 1.

### Phấn Tấn — `fenxun`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 1 lá và lựa chọn 1 người khác, khoảng cách từ bạn đến họ là 1 trong lượt này.

## StrategicAdvantagePackage

Nguồn: `lang\vi_VN\Package\StrategicAdvantagePackage.lua`

Tên nhân vật nhận diện được: Hộ Tâm Kính (`Breastplate`); Minh Quang Khải (`IronArmor`); Mộc Ngưu Lưu Mã (`WoodenOx`).

### Thanh Long Yển Nguyệt Đao — `Blade`

Bài Trang bị - Vũ khí

Tầm đánh: 3
Kỹ năng: Tỏa định kỹ: Khi bạn sử dụng [Sát], mục tiêu của lá [Sát] này không thể mở tướng cho đến khi [Sát] này kết toán xong

### Phương Thiên Hoạ Kích — `Halberd`

Bài Trang bị - Vũ khí

Tầm đánh: 4
Kỹ năng: Sau khi bạn chỉ định mục tiêu cho [Sát], bạn có thể chỉ định ở các thế lực xác định khác với mục tiêu, mỗi thế lực một người, đồng thời có thể chọn những người không có thế lực, lệnh họ trở thành mục tiêu của [Sát] này;
▶ Sau khi 1 mục tiêu sử dụng [Thiểm] triệt tiêu [Sát] này, lệnh cho [Sát] này không có hiệu quả với những mục tiêu còn lại.

### Hộ Tâm Kính — `Breastplate`

Bài Trang bị - Phòng cụ

Kỹ năng: Khi bạn nhận sát thương, nếu số sát thương ≥ số máu hiện tại của bạn, bạn có thể đưa lá này từ vùng trang bị vào chồng bài bỏ để chặn sát thương này.

### Minh Quang Khải — `IronArmor`

Bài Trang bị - Phòng cụ

Kỹ năng: Tỏa định kỹ:
• Khi bạn trở thành mục tiêu của [Hỏa Thiêu Liên Doanh]/[Hỏa Công]/[Sát Hỏa], hủy bỏ mục tiêu đối với bạn.
• Nếu bạn thuộc tiểu thế lực, bạn không thể nhận trạng thái xích.

### Mộc Ngưu Lưu Mã — `WoodenOx`

Bài Trang bị - Bảo vật

Kỹ năng:
• Một lần trong giai đoạn ra bài, nếu số lá trong [Mộc Ngưu Lưu Mã] < 5, bạn có thể đặt úp 1 lá trên tay vào [Mộc Ngưu Lưu Mã], sau đó bạn có thể chuyển [Mộc Ngưu Lưu Mã] sang vùng trang bị của người khác.
• Bạn có thể sử dụng hoặc đánh ra bài trên [Mộc Ngưu Lưu Mã] như bài trên tay.
• Khi bạn mất [Mộc Ngưu Lưu Mã], nếu lá này không chuyển sang vùng trang bị khác, đưa tất cả lá trong [Mộc Ngưu Lưu Mã] vào chồng bài bỏ.

### Ngọc Tỉ — `JadeSeal`

Bài Trang bị - Bảo vật

Kỹ năng: Tỏa định kỹ: Nếu bạn đã có thế lực:
• Thế lực của bạn là Đại thế lực duy nhất, tất cả thế lực khác không có [Ngọc Tỉ] là Tiểu Thế Lực.
• Giai đoạn rút bài, bạn rút thêm 1 lá.
• Khi bắt đầu giai đoạn ra bài, bạn xem như sử dụng 1 lá [Tri Bỉ Tri Kỉ].


### Thuỷ Yêm Thất Quân — `drowning`

Bài công cụ

Lựa chọn: 1 người khác có bài trong vùng trang bị
Mục tiêu: Người đã chọn
Hiệu quả: Mục tiêu lựa chọn bỏ tất cả bài trong vùng trang bị hoặc nhận 1 sát thương Lôi.

### Hỏa Thiêu Liên Doanh — `burning_camps`

Bài công cụ

Mục tiêu: Tất cả người cùng đội hình với người phía sau bạn.
Hiệu quả: Bạn gây 1 sát thương Hỏa đối với mục tiêu. 

### Điệu Hổ Ly Sơn — `lure_tiger`

Bài công cụ

Lựa chọn: 1-2 người khác
Mục tiêu: Người đã chọn
Hiệu quả: Trong lượt này, mục tiêu không tính khoảng cách, vị trí; không thể sử dụng bài; không thể bị chỉ định làm mục tiêu của bài; không thể thay đổi số máu.

### Lục Lực Đồng Tâm — `fight_together`

Bài công cụ

Lựa chọn: 1 người thuộc đại thế lực hoặc tiểu thế lực
Mục tiêu: Tất cả người thuộc cùng cấp độ thế lực với người đã chọn.
Hiệu quả: Nếu mục tiêu đang có trạng thái xích, họ rút 1 lá; nếu không, họ nhận trạng thái xích.
Trùng Chú: Có thể đưa lá này vào chồng bài bỏ để rút 1 lá.

### Liên Quân Thịnh Yến — `alliance_feast`

Bài công cụ

Lựa chọn: 1 người có thế lực xác định khác bạn
Mục tiêu: Bạn và tất cả người cùng thế lực với người đã chọn.
Hiệu quả: Nếu mục tiêu là:
*Bạn: Chọn rút số bài và hồi số máu tùy ý với tổng bằng số người của thế lực đã chọn.
* Không phải bạn: Họ rút 1 lá và thoát trạng thái xích.

### Hiệp Thiên Tử Dĩ Lệnh Chư Hầu — `threaten_emperor`

Bài công cụ

Mục tiêu: Bạn
Điều kiện: Bạn thuộc đại thế lực và đang trong giai đoạn ra bài của bạn
Hiệu quả: Bạn kết thúc giai đoạn ra bài;
▶ Khi kết thúc giai đoạn bỏ bài, bạn có thể bỏ 1 lá trên tay để nhận thêm một lượt sau lượt này.

### Sắc lệnh — `imperial_order`

Bài công cụ

Mục tiêu: Tất cả người không có thế lực.
Hiệu quả: Mục tiêu chọn 1 mục:
1. Mở 1 tướng và rút 1 lá;
2.Bỏ 1 trang bị;
3. Mất 1 máu.
Hiệu ứng thêm: Khi lá này tiến vào chồng bài bỏ không phải do sử dụng, lá này bị loại bỏ khỏi trận đấu, sau đó đưa [Chiếu Thư] vào đáy chồng bài rút;
▶ Khi kết thúc lượt này, tất cả người không có thế lực có thế lực giải quyết hiệu quả của lá này.

## TransformationPackage

Nguồn: `lang\vi_VN\Package\TransformationPackage.lua`

Tên nhân vật nhận diện được: Tuân Du (`xunyou`); Biện Phu Nhân (`bianhuanghou`); Lý Giác & Quách Tỷ (`lijueguosi`); Tả Từ (`new_zuoci`); Sa Ma Kha (`shamoke`); Mã Tắc (`masu`); Lăng Thống (`lingtong`); Lữ Phạm (`lvfan`); Tôn Quyền - Quân (`lord_sunquan`).

### Kỳ sách — `qice`

Một lần trong giai đoạn ra bài, bạn có thể chuyển hóa sử dụng tất cả bài trên tay thành 1 lá công cụ phổ thông (Số mục tiêu không vượt quá số lá đem sử dụng);
▷ Bạn có thể đổi Phó tướng.

### Trí Ngu — `zhiyu`

Sau khi bạn nhận sát thương, bạn có thể rút 1 lá và mở tất cả bài trên tay, nếu tất cà đều cùng màu, nguồn sát thương bỏ 1 lá trên tay.

### Văn Ngụy — `wanwei`

Khi bài của bạn bị người khác chỉ định để thu lấy hoặc bỏ, bạn có thể đổi thành tự chọn lá của bạn.

### Ước Kiệm — `yuejian`

Tỏa định kỹ: Khi bắt đầu giai đoạn bỏ bài của người cùng thế lực, nếu lượt này họ không sử dụng bài chọn người thế lực khác làm mục tiêu, bạn lệnh giới hạn trữ bài của họ bằng với giới hạn máu.

### Hung Toán — `xiongsuan`

Hạn định kỹ: Giai đoạn ra bài, bạn có thể bỏ 1 lá bài trên tay và chọn 1 người cùng thế lực, thực hiện lần lượt:
- Bạn gây 1 sát thương cho họ;
- Bạn rút 3 lá;
- Bạn chọn 1 Hạn định kỹ đã phát động của họ;
▶ Khi kết thúc lượt này, thêm 1 giới hạn phát động Hạn định kỹ đó.

### Dịch Quỷ — `yigui`

• Sau khi bạn mở tướng này lần đầu tiên, bạn nhận 2 lá từ chồng bài tướng đặt lên tướng này, gọi là [Hồn].
• Khi bạn cần sử dụng lá cơ bản hoặc công cụ phổ thông có mục tiêu, nếu bạn chưa sử dụng lá đó bằng kỹ năng này trong lượt này, bạn có thể bỏ 1 [Hồn], xem như bạn sử dụng lá đó;
▷ Bạn không thể chỉ định người thế lực gốc khác với [Hồn] làm mục tiêu của lá này.

### Cấp Hồn — `jihun`

Sau khi bạn nhận sát thương hoặc sau khi 1 người thế lực xác định khác với bạn thoát khỏi trạng thái hấp hối, bạn có thể nhận 1 lá từ chồng bài tướng đặt lên tướng này, gọi là [Hồn].

### Tật Lê — `jili`

Khi bạn sử dụng/đánh ra bài, nếu lá này là lá thứ X mà bạn sử dụng/đánh ra trong lượt này, bạn có thể rút X lá (X là tầm đánh của bạn).

### Tán Dao — `sanyao`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 1 lá và chọn 1 người nhiều máu nhất, bạn gây 1 sát thương cho họ.

### Chế Man — `zhiman`

Khi bạn gây sát thương cho người khác, bạn có thể chặn sát thương này lại, thực hiện lần lượt:
- Bạn thu lấy 1 lá trong vùng trang bị hoặc phán xét của họ;
- Nếu họ cùng thế lực với bạn, bạn có thể lệnh họ đổi Phó tướng.

### Toàn Lược — `xuanlue`

Sau khi bạn mất bài trong vùng trang bị, bạn có thể bỏ 1 lá của người khác.

### Dũng Tiến — `yongjin`

Hạn định kỹ: Giai đoạn ra bài, bạn có thể phát động kỹ năng này: Tối đa 3 lần, bạn có thể di chuyển 1 trang bị trên bàn chơi.

### Điều Độ — `diaodu`

• Khi 1 người cùng thế lực với bạn sử dụng trang bị, họ có thể rút 1 lá.
• Đầu giai đoạn ra bài, bạn có thể thu lấy 1 lá trong vùng trang bị của 1 người cùng thế lực, sau đó, nếu người bị thu lấy là:
 * Bạn: Bạn giao lá đó cho 1 người khác;
 * Không phải bạn: Bạn có thể giao lá đó cho 1 người khác ngoại trừ họ.

### Điển Tài — `diancai`

Khi kết thúc giai đoạn ra bài của người khác, nếu bạn đã mất ít nhất X lá trong giai đoạn này (X là số máu của bạn, tối thiểu 1), bạn có thể bổ sung bài trên tay tới giới hạn máu;
▷ Bạn có thể đổi Phó tướng.

### Gia Hỏa — `jiahe`

Quân chủ kỹ, Tỏa định kỹ: Bạn có »Duyên Giang Phong Hỏa Đồ«.

»Duyên Giang Phong Hỏa Đồ«:
• Một lần trong giai đoạn ra bài của mỗi người thế lực Ngô, họ có thể đặt 1 trang bị lên »Duyên Giang Phong Hỏa Đồ«, gọi là [Phong Hỏa].
• Khi bắt đầu giai đoạn chuẩn bị của người thế lực Ngô, họ có thể nhận 1 kỹ năng tùy theo số [Phong Hỏa]:
* 1+: »Anh Tư«;
* 2+: »Hảo Thi«;
* 3+: »Thiệp Liệp«;
* 4+: »Độ Thế«;
▷ Nếu có 5 [Phong Hỏa] trở lên, họ có thể nhận thêm 1 kỹ năng khác.
• Tỏa định kỹ: Sau khi bạn nhận sát thương từ lá bài, đưa 1 [Phong Hỏa] vào chồng bài bỏ.

### Liễm Tư — `lianzi`

Một lần trong giai đoạn ra bài, bạn có thể bỏ 1 lá trên tay, sau đó lật ra X lá trên đầu chồng bài rút (X là số [Phong Hỏa] cộng với số lá trong vùng trang bị của những người thế lực Ngô), bạn thu lấy những lá cùng loại với lá bạn bỏ;
▷ Nếu trong 1 lần bạn thu lấy > 3 lá, bạn mất kỹ năng này và nhận kỹ năng »Chế Hành«.

### Tư Bảo — `jubao`

Tỏa định kỹ:
• Người khác không thể thu lấy bảo vật trong khu trang bị của bạn.
• Khi bắt đầu giai đoạn kết thúc, nếu trên bàn chơi hoặc chồng bài bỏ có [Định Lan Dạ Minh Châu], bạn rút 1 lá, sau đó thu lấy 1 lá của người đang trang bị [Định Lan Dạ Minh Châu].

### Duyên Giang Phong Hỏa Đồ — `flamemap`

• Một lần trong giai đoạn ra bài của mỗi người thế lực Ngô, họ có thể đặt 1 trang bị lên »Duyên Giang Phong Hỏa Đồ«, gọi là [Phong Hỏa].
• Khi bắt đầu giai đoạn chuẩn bị của người thế lực Ngô, họ có thể nhận 1 kỹ năng tùy theo số [Phong Hỏa]:
* 1+: »Anh Tư«;
* 2+: »Hảo Thi«;
* 3+: »Thiệp Liệp«;
* 4+: »Độ Thế«;
▷ Nếu có 5 [Phong Hỏa] trở lên, họ có thể nhận thêm 1 kỹ năng khác.
• Tỏa định kỹ: Sau khi bạn nhận sát thương từ lá bài, đưa 1 [Phong Hỏa] vào chồng bài bỏ.

### Thiệp Liệp — `shelie`

Khi bắt đầu giai đoạn rút bài, bạn có thể không rút bài, đổi thành lật ra 5 lá trên đầu chồng bài rút, thu lấy trong đó mỗi chất 1 lá.

### Định Lan Dạ Minh Châu — `LuminousPearl`

Bài Trang bị - Bảo vật

Kỹ năng: Tỏa định kỹ:
* Nếu bạn đã có »Chế Hành«, không giới hạn số lá bỏ đi trong 1 lần phát động »Chế Hành«;
* Nếu bạn không có kỹ năng »Chế Hành«, xem như bạn có »Chế Hành«.
