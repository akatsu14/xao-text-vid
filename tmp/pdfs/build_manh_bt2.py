from pathlib import Path
helper = Path('tmp/pdfs/build_manh_report.py').read_text(encoding='utf-8').split('# Trang 1')[0]
helper = helper.replace('output/baitap1_manh', 'output/baitap2_manh')
exec(helper, globals())
doc.core_properties.title = 'Pipeline hồi quy với tiền xử lý và giảm chiều PCA'
CV = {r['model']:r for r in R['cv']}
TE = {r['model']:r for r in R['test']}


def plot(name, caption, width=15.5):
    cap(caption)
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.add_run().add_picture(str(BASE/'ket_qua'/name), width=Cm(width))


def code_line(text):
    para = doc.add_paragraph()
    para.paragraph_format.space_after = Pt(0)
    para.paragraph_format.space_before = Pt(0)
    para.paragraph_format.line_spacing = 1.05
    r = para.add_run(text if text else ' ')
    r.font.name = 'Consolas'
    r.font.size = Pt(8.5)


def mean_sd(row, metric, n=2):
    return fmt(row[metric+'_mean'], n)+' ± '+fmt(row[metric+'_std'], n)


for text in ['BÀI TẬP 2', 'HỌC PHẦN NHẬN DẠNG MẪU']:
    x = doc.add_paragraph(text); x.alignment = WD_ALIGN_PARAGRAPH.CENTER
    x.runs[0].bold = True
doc.add_paragraph()
x = doc.add_paragraph('Pipeline hồi quy với tiền xử lý và giảm chiều PCA', 'Title')
x.alignment = WD_ALIGN_PARAGRAPH.CENTER
x.paragraph_format.space_after = Pt(20)
x = doc.add_paragraph('Dự báo chỉ số tiến triển bệnh trên bộ dữ liệu Diabetes', 'Subtitle')
x.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()
for text in ['Sinh viên  Lương Đức Mạnh', 'Mã học viên  B26CHKH068', 'Lớp  M26CQKH03-B', 'Năm học  2026 - 2027']:
    x = doc.add_paragraph(text); x.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()
h('Tóm tắt', 2)
p('Báo cáo xây dựng pipeline dự báo target định lượng của bộ dữ liệu Diabetes gồm 442 mẫu và 10 đặc trưng. Sáu phương án được so sánh: dự báo trung bình, hồi quy tuyến tính, Ridge, SVR, Ridge có PCA và SVR có PCA. Dữ liệu được tách thành 353 mẫu Train và 89 mẫu Test; lựa chọn mô hình dựa trên CV lồng nhau ở phần Train.')
p('SVR không dùng PCA có RMSE CV trung bình thấp nhất là 56,77, với độ lệch chuẩn 1,36. Trên Test, mô hình đạt MAE 36,17, RMSE 47,84 và R² 0,5461. PCA cần 8 thành phần để giữ trên 95% phương sai Train, nhưng không cải thiện đồng đều chất lượng dự báo. Chênh lệch giữa các mô hình hồi quy nhỏ nên kết quả không chứng minh ưu thế thống kê của một họ mô hình.')
p('Mã nguồn, dữ liệu đã chia, điểm từng fold, dự báo Test và biểu đồ được cung cấp kèm báo cáo để tái tạo kết quả. Thực nghiệm nhằm đánh giá pipeline học máy trên dữ liệu chuẩn; không đánh giá hiệu quả sử dụng trong lâm sàng.')

page('1 Bài toán và bộ dữ liệu')
p('Đề Bài tập 2 yêu cầu chọn dữ liệu có target liên tục, xây dựng chương trình dự báo, so sánh baseline với các mô hình hồi quy và kiểm tra tác động của PCA. Bài này sử dụng Diabetes tích hợp trong scikit-learn, có 442 mẫu và 10 biến đầu vào [1]. Target là chỉ số định lượng về tiến triển bệnh sau một năm; dù dữ liệu ghi bằng số nguyên, đây là đại lượng cần hồi quy, không phải nhãn phân lớp.')
cap('Bảng 1. Biến đầu vào và target')
table(['Biến','Ý nghĩa trong dữ liệu'],[['age','Tuổi'],['sex','Biến giới tính đã mã hóa trong bộ dữ liệu'],['bmi','Chỉ số khối cơ thể'],['bp','Huyết áp trung bình'],['s1, s2, s3','Các chỉ số cholesterol toàn phần, LDL và HDL'],['s4','Tỷ số cholesterol toàn phần trên HDL'],['s5','Biến ltg theo mô tả dữ liệu; giữ nguyên giá trị nguồn'],['s6','Chỉ số đường huyết'],['target','Chỉ số định lượng tiến triển bệnh sau một năm']], [3.2,13.5])
p('Chương trình gọi load_diabetes(scaled=False) để nhận các biến chưa chuẩn hóa bởi hàm tải dữ liệu. Điều này cho phép StandardScaler học trung bình và độ lệch chuẩn chỉ từ Train hoặc phần huấn luyện của từng fold. Không dùng chế độ scaled=True mặc định để tránh đưa thống kê của cả bộ dữ liệu vào bước tiền xử lý [1].')
p('Kiểm tra dữ liệu cho thấy không có giá trị thiếu, không có giá trị vô hạn và không có hai hàng X trùng hoàn toàn. Target nằm trong khoảng 25 đến 346. Không loại ngoại lệ hoặc chọn đặc trưng dựa trên kết quả Test. Biến sex được giữ dưới dạng mã số đã cung cấp; bài không suy diễn ý nghĩa của từng mã.')
p('sample_id trong các tệp CSV là chỉ số hàng gốc bắt đầu từ 0, chỉ dùng để đối chiếu chia tập. Đây không phải đặc trưng của mô hình hay định danh bệnh nhân. Tệp train.csv và test.csv lưu đúng 10 biến theo thứ tự age, sex, bmi, bp, s1, s2, s3, s4, s5, s6 cùng target.')

page('2 Pipeline và thiết kế đánh giá')
h('2 1 Tiền xử lý bên trong mô hình',2)
p('Pipeline thực hiện theo thứ tự: điền thiếu bằng trung vị → chuẩn hóa StandardScaler → PCA nếu được bật → mô hình hồi quy. Bộ dữ liệu hiện không thiếu, nên SimpleImputer không làm thay đổi các giá trị; bước này giữ cấu trúc xử lý nhất quán. Target được giữ nguyên thang đo.')
eq('z = ', ('x − μ','σ'))
p('μ và σ được ước lượng riêng cho từng cột trên phần dữ liệu đang dùng để fit. Validation/Test chỉ được transform bằng các tham số đã học. PCA dùng SVD đầy đủ và whiten=False. PCA tự căn giữa nhưng không tự chuẩn hóa thang đo từng biến, nên StandardScaler được đặt trước PCA [2, 3].')
h('2 2 Tách Test trước khi chọn mô hình',2)
p('Tách ngẫu nhiên 80% Train và 20% Test với random_state = 68, thu được 353 và 89 mẫu. Test không tham gia chọn siêu tham số, số thành phần PCA hoặc họ mô hình. Baseline cũng chỉ học giá trị trung bình target của phần huấn luyện.')
cap('Bảng 2. Vai trò của các vòng đánh giá')
table(['Bước','Thiết lập','Dữ liệu dùng'],[['Tách Test','test_size = 0,2; seed = 68','442 mẫu ban đầu'],['CV ngoài','KFold 5; shuffle; seed = 70','353 mẫu Train'],['CV trong','KFold 3; shuffle; seed = 69','Phần train của từng fold ngoài'],['Fit cuối','Tìm tham số lại bằng CV trong','Toàn bộ 353 mẫu Train'],['Đánh giá cuối','Một lượt sau khi chốt họ mô hình','89 mẫu Test']], [3.4,6.8,6.5])
p('Ở mỗi fold ngoài, GridSearchCV chọn cấu hình có RMSE CV trong thấp nhất rồi fit lại trên phần train của fold ngoài. Mô hình đó dự báo phần validation ngoài để tính MAE, RMSE và R². Các phương án dùng chung năm cách chia ngoài, giúp so sánh trên cùng tập validation. Pipeline bảo đảm imputer, scaler và PCA đều được fit lại trong từng lượt [2, 4].')
p('Điểm CV ngoài đánh giá quy trình tìm tham số trong từng họ mô hình. Vì còn dùng các điểm này để chọn giữa sáu họ, điểm của họ thắng vẫn có thể chịu thiên lệch lựa chọn; tập Test giữ riêng là đánh giá cuối. Bài không coi trung bình ± SD của năm fold là khoảng tin cậy hay kiểm định khác biệt có ý nghĩa thống kê.')

page('3 Mô hình và tiêu chí lựa chọn')
cap('Bảng 3. Các phương án và không gian tìm kiếm')
table(['Tên','Mô hình và siêu tham số'],[['Mean','DummyRegressor(strategy="mean")'],['Linear','LinearRegression có hệ số chặn'],['Ridge','α ∈ {0,1; 1; 10; 100}; solver="svd"'],['Ridge_PCA','Như Ridge; k ∈ {2; 4; 6; 8; 0,95}'],['SVR','RBF; C ∈ {10; 100; 1000}; γ ∈ {0,01; 0,1}'],['SVR_PCA','Như SVR; k ∈ {2; 4; 6; 8; 0,95}']], [3.8,12.9])
p('SVR cố định epsilon = 0,1 và không chuẩn hóa target. Giá trị k = 0,95 có nghĩa là chọn đủ số thành phần để giải thích trên 95% phương sai của phần dữ liệu dùng để fit PCA, không phải giữ 0,95 thành phần [3]. Các mô hình PCA có thể chọn k khác nhau giữa các fold.')
p('Linear tối thiểu hóa tổng bình phương sai số. Ridge bổ sung phạt L2 cho hệ số, giúp kiểm soát hệ số lớn khi các biến tương quan. SVR với kernel RBF mô tả quan hệ phi tuyến; C và γ điều chỉnh mức phạt và phạm vi tác động của kernel. Các họ mô hình chỉ được so sánh trong phạm vi lưới tham số đã nêu.')
h('3 1 Các thước đo',2)
eq('MAE = ', ('∑|y − ŷ|','n'))
# Căn bậc hai với phân số bên trong bằng phương trình Word.
para=doc.add_paragraph(); para.alignment=WD_ALIGN_PARAGRAPH.CENTER
om=OxmlElement('m:oMath'); om.append(mathrun('RMSE = '))
rad=OxmlElement('m:rad'); prop=OxmlElement('m:radPr')
hide=OxmlElement('m:degHide'); hide.set(qn('m:val'),'1'); prop.append(hide); rad.append(prop)
rad.append(OxmlElement('m:deg')); e=OxmlElement('m:e'); f=OxmlElement('m:f')
for tag,text in [('num','∑(y − ŷ)²'),('den','n')]:
    z=OxmlElement('m:'+tag); z.append(mathrun(text)); f.append(z)
e.append(f); rad.append(e); om.append(rad); para._p.append(om)
eq('R² = 1 − ', ('∑(y − ŷ)²','∑(y − ȳ)²'))
p('Các tổng chạy trên n mẫu của tập đang đánh giá; ȳ là trung bình target của chính tập đó. MAE và RMSE cùng đơn vị với target, càng thấp càng tốt; RMSE nhạy hơn với sai số lớn. R² càng cao càng tốt và có thể âm khi dự báo kém hơn dùng trung bình của tập đánh giá. R² không phải phần trăm dự đoán chính xác.')
h('3 2 Quy tắc chốt họ mô hình',2)
p('Tiêu chí chính là RMSE CV ngoài trung bình nhỏ nhất. Nếu bằng nhau, lần lượt xét MAE trung bình nhỏ hơn, SD RMSE nhỏ hơn, rồi R² trung bình lớn hơn. Báo cáo vẫn đối chiếu tất cả thước đo để nhận diện đánh đổi. SD được tính theo công thức độ lệch chuẩn mẫu với ddof = 1 trên năm fold ngoài.')

page('4 Kết quả cross validation')
cap('Bảng 4. Trung bình ± SD trên 5 fold CV ngoài')
table(['Mô hình','MAE','RMSE','R²'], [[r['model'],mean_sd(r,'MAE'),mean_sd(r,'RMSE'),mean_sd(r,'R2',4)] for r in R['cv']], [3.6,4.25,4.25,4.6])
plot('cv_comparison.png','Hình 1. RMSE CV ngoài với thanh sai số biểu diễn SD')
p('Các mô hình hồi quy giảm rõ sai số so với baseline Mean: RMSE khoảng 56,77–57,27 so với 78,66. SVR có RMSE trung bình 56,77, MAE trung bình 46,57 và R² trung bình 0,4667, tốt nhất theo các trung bình này nên được chọn trước khi xem Test.')
p('SVR_PCA có SD RMSE nhỏ nhất trong các phương án hồi quy là 1,17, nhưng RMSE trung bình cao hơn SVR khoảng 0,46. Ridge_PCA chỉ cải thiện RMSE trung bình khoảng 0,11 so với Ridge. Các khoảng biến động chồng lấp, vì vậy không có căn cứ từ năm fold để khẳng định SVR vượt trội có ý nghĩa thống kê.')
p('Baseline Mean có R² CV trung bình âm vì giá trị trung bình học từ phần train của fold không nhất thiết trùng trung bình của validation. Đây là hành vi hợp lệ. Toàn bộ điểm từng fold, tham số chọn trong mỗi fold và dự báo ngoài fold được lưu trong cv_folds.csv và oof_predictions.csv.')

page('5 PCA thay đổi kết quả như thế nào')
p('PCA tìm các hướng có phương sai lớn trong X đã chuẩn hóa và chiếu dữ liệu lên k hướng đầu. Với W chứa k vectơ trực chuẩn, phép chiếu là Z = XW. PCA không dùng target khi tìm hướng, nên thành phần có phương sai nhỏ vẫn có thể chứa tín hiệu hữu ích cho hồi quy.')
cap('Bảng 5. Khảo sát riêng PCA với Ridge cố định α = 1')
table(['k','Phương sai Train tích lũy','RMSE CV trung bình ± SD'], [[a['k'],fmt(R['pca_variance'][a['k']-1]*100,2)+'%',fmt(a['RMSE_mean'],2)+' ± '+fmt(a['RMSE_std'],2)] for a in R['ablation']], [2,6.3,8.4])
plot('pca_effect.png','Hình 2. Phương sai giữ lại và sai số khi thay số thành phần PCA')
p('Trên toàn bộ Train, 7 thành phần giữ 94,78% phương sai, chưa đạt 95%; 8 thành phần giữ 99,10% nên đạt điều kiện. Hai thành phần chỉ giữ 55,26% phương sai và cho RMSE CV 64,21. Trong khảo sát cố định α = 1, k = 6 có RMSE CV thấp nhất là 56,66 dù chỉ giữ 89,35% phương sai.')
p('Bảng 5 là khảo sát có kiểm soát: α cố định, chỉ thay k; scaler và PCA vẫn fit lại theo từng fold. Cột phương sai là mô tả PCA fit trên toàn bộ Train, không phải thống kê được dùng trước cho các fold. Không dùng khảo sát này để đổi lại họ mô hình đã chọn hoặc đối chiếu trực tiếp điểm nhỏ nhất với quy trình nested CV ở Bảng 4.')
p('Trong tìm kiếm tham số cuối trên Train, Ridge_PCA chọn k = 6, α = 10; SVR_PCA chọn k = 4, C = 100, γ = 0,01. Kiểm tra bổ sung cho thấy Ridge α = 1 dùng đủ 10 thành phần PCA và Ridge không PCA cho dự báo Test lệch tối đa khoảng 6,82 × 10⁻¹³. Điều này phù hợp với PCA đầy đủ chỉ quay hệ trục khi không whitening.')

page('6 Đánh giá trên tập Test giữ riêng')
cap('Bảng 6. Kết quả trên 89 mẫu Test sau khi fit lại trên Train')
table(['Mô hình','MAE','RMSE','R²'], [[r['model'],fmt(r['MAE'],2),fmt(r['RMSE'],2),fmt(r['R2'],4)] for r in R['test']], [4.4,4.1,4.1,4.1])
plot('test_diagnostics.png','Hình 3. Dự báo và phần dư của SVR trên tập Test')
p('SVR được chọn từ CV đạt MAE 36,17, RMSE 47,84 và R² 0,5461. So với Mean, RMSE Test giảm khoảng '+fmt((TE['Mean']['RMSE']-TE['SVR']['RMSE'])/TE['Mean']['RMSE']*100,2)+'%. Linear có RMSE Test thấp hơn SVR khoảng 0,13, nhưng đây là kết quả quan sát sau cùng; bài giữ lựa chọn SVR theo quy tắc CV đã chốt.')
p('PCA làm RMSE Test của Ridge tăng từ 47,72 lên 48,46 và của SVR tăng từ 47,84 lên 50,08. Do các pipeline được tìm tham số riêng, đây là so sánh các quy trình đã tối ưu trong lưới, không tách riêng tác động của k. Khảo sát cố định α ở Bảng 5 bổ sung góc nhìn đó.')
p('Phần dư được định nghĩa là y thật trừ dự đoán. Độ phân tán còn lớn cho thấy mô hình chưa dự báo chính xác từng mẫu. Biểu đồ dùng để mô tả sai số, không được dùng để chỉnh tiếp tham số rồi công bố lại cùng điểm Test. Test thấp hơn CV có thể do khác biệt của lần chia hữu hạn; không đủ để kết luận mô hình luôn đạt mức sai số này.')

page('7 Ví dụ dự báo và giới hạn')
h('7 1 Một quan sát chưa dùng để fit',2)
p('Mẫu có sample_id = 400 thuộc Test, được chọn theo vị trí đầu tiên trong tập Test của lần chia cố định, không được chọn vì có sai số nhỏ. Các giá trị đầu vào dưới đây giữ đúng thứ tự mà chương trình dự báo yêu cầu.')
cap('Bảng 7. Đầu vào của mẫu minh họa')
table(['age','sex','bmi','bp','s1','s2','s3','s4','s5','s6'], [R['example']['x']], [1.5,1.25,1.65,1.65,1.65,1.85,1.65,1.25,2.55,1.7])
p('SVR được fit trên 353 mẫu Train dự báo target khoảng 178,26; target thật của mẫu là 175,00, sai số tuyệt đối khoảng 3,26. Đây chỉ là một ví dụ về luồng dự báo và không đại diện cho sai số trung bình của 89 mẫu Test.')
p('Tệp predict_new.py chỉ đọc Train, họ mô hình và cấu hình cuối đã chọn để fit lại rồi dự báo 10 giá trị đầu vào. Target của mẫu mới không được truyền vào mô hình. Lệnh python predict_new.py chạy ví dụ mặc định; cũng có thể cung cấp 10 số sau tên tệp.')
h('7 2 Giới hạn',2)
p('Diabetes là bộ dữ liệu nhỏ, chỉ có 89 mẫu Test trong lần chia này. Kết quả phụ thuộc vào cách chia và lưới tham số; một lần 5-fold CV không bao quát mọi biến động có thể có. SD giữa fold là chỉ báo độ ổn định mô tả, các fold không phải các thí nghiệm hoàn toàn độc lập.')
p('Tách ngẫu nhiên giả định các hàng phù hợp để đánh giá theo cách chia này. Dữ liệu cung cấp không có thông tin nhóm hoặc thời gian đủ để kiểm chứng khái quát sang bệnh viện khác hay quần thể khác. Các chỉ số này không đánh giá hiệu quả sử dụng trong thực hành y khoa.')
p('PCA giảm số chiều nhưng làm các thành phần khó diễn giải theo từng biến gốc. Giữ 95% phương sai không bảo đảm giữ 95% thông tin về target. Bài không thực hiện lựa chọn đặc trưng bằng target, không thử toàn bộ mô hình có thể có và không kiểm định ưu thế thống kê giữa các phương án gần nhau.')
h('7 3 Kết luận',2)
p('Pipeline đã đáp ứng yêu cầu tiền xử lý, baseline, so sánh hồi quy và đánh giá PCA bằng MAE, RMSE, R² cùng biến động CV. SVR không PCA được chọn theo RMSE CV trung bình thấp nhất; PCA hữu ích để khảo sát giảm chiều nhưng chưa cải thiện kết quả Test trong hai cặp mô hình của thực nghiệm. Quyết định giữ hoặc bỏ PCA cần dựa vào đánh giá dự báo, thay vì chỉ dựa vào tỷ lệ phương sai.')

page('8 Tái tạo kết quả và tài liệu tham khảo')
h('8 1 Cách chạy',2)
p('Môi trường đã kiểm chứng: Python '+R['versions']['python']+', NumPy '+R['versions']['numpy']+', SciPy '+R['versions']['scipy']+', scikit-learn '+R['versions']['sklearn']+' và matplotlib 3.11.1. Tệp requirements.txt cố định phiên bản thư viện. Dữ liệu Diabetes đi kèm scikit-learn nên không cần tải dữ liệu từ Internet khi chạy sau khi cài thư viện.')
for cmd in ['python -m pip install -r requirements.txt','python regression_pca.py','python plot_results.py','python predict_new.py']:
    x=doc.add_paragraph(); x.add_run(cmd).font.name='Consolas'; x.runs[0].font.size=Pt(10)
h('8 2 Tệp kết quả và kiểm tra',2)
p('Thư mục ket_qua chứa Train/Test, danh sách fold, điểm và dự báo CV, lựa chọn mô hình, siêu tham số cuối, dự báo Test, khảo sát PCA và ba hình. results.json ghi phiên bản cùng SHA-256 của dữ liệu để đối chiếu. Mã regression_pca.py đầy đủ được in ở Phụ lục A; mã vẽ và dự báo nằm trong gói đi kèm.')
p('Các kiểm tra tự động gồm: số mẫu và kích thước dữ liệu, Train/Test không giao nhau, dữ liệu hữu hạn, median và mean của preprocessing cuối khớp Train, tính lại MAE/RMSE/R² bằng NumPy và kiểm tra Ridge tương đương khi PCA giữ đủ chiều. Các kiểm tra đã đạt trong lần chạy tạo báo cáo.')
p('Muốn khảo sát khác, thay dữ liệu, lưới hoặc seed rồi tạo một bộ kết quả mới. Không được chọn cấu hình dựa trên Test hiện tại và tiếp tục xem đó là đánh giá độc lập. Chênh lệch rất nhỏ ở chữ số cuối có thể xuất hiện giữa môi trường đại số tuyến tính khác nhau.')
h('Tài liệu tham khảo',2)
refs=[
    '[1] scikit-learn. load_diabetes và mô tả Diabetes đi kèm gói dữ liệu. https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html',
    '[2] scikit-learn. Common pitfalls and recommended practices, mục Data leakage. https://scikit-learn.org/stable/common_pitfalls.html',
    '[3] scikit-learn. PCA API reference. https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html',
    '[4] scikit-learn. Nested versus non-nested cross-validation. https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html',
    'Nguồn yêu cầu: Baitap2.pdf do học viên cung cấp. Các bảng và biểu đồ kết quả được tạo bằng mã thực nghiệm của bài này. Tài liệu trực tuyến truy cập ngày 07/09/2026.'
]
for text in refs:
    x=p(text)
    for run in x.runs:run.font.size=Pt(10)

lines=(BASE/'regression_pca.py').read_text(encoding='utf-8').splitlines()
chunks=[lines[i:i+42] for i in range(0,len(lines),42)]
for i,chunk in enumerate(chunks):
    page('Phụ lục A Mã thí nghiệm đầy đủ' if i==0 else f'Phụ lục A Mã thí nghiệm phần {i+1}')
    if i==0:
        p('Tệp regression_pca.py. Các phần dưới đây nối tiếp nhau, không lược bỏ mã. Có thể chạy trực tiếp tệp đi kèm để tránh lỗi sao chép từ PDF.')
    for line in chunk:code_line(line)
for root in [doc.styles.element,doc.element]:
    for border in list(root.iter(qn('w:pBdr'))):border.getparent().remove(border)
doc.save(BASE/'B26CHKH068_Luong_Duc_Manh_BT2_HoanChinh.docx')
print('Saved BT2 DOCX;',len(lines),'source lines;',len(chunks),'appendix pages')
