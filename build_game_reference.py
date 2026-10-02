from pathlib import Path
import re
import html

root = Path(__file__).resolve().parent
game = root / 'QSanguosha-LangKhach-QuocChien-2.3.41.2' / 'QSanguosha-LangKhach-QuocChien'
literal = r'"(?:\\.|[^"\\])*"'
entry = re.compile(r'\["([^"\n]+)"\]\s*=\s*(' + literal + r'(?:\s*\.\.\s*' + literal + r')*)')

def decode(expr):
    parts = re.findall(literal, expr)
    value = ''.join(re.sub(r'\\([nrt"\\])', lambda m: {'n':'\n','r':'\r','t':'\t','"':'"','\\':'\\'}[m[1]], p[1:-1]) for p in parts)
    return html.unescape(re.sub(r'</?[A-Za-z][^>]*>', '', value))

lines = ['# Tra cứu nhân vật, kỹ năng và bài — Quốc Chiến 2.3.41.2', '',
         'Trích từ các bảng dịch tiếng Việt của bộ game trên máy. Đây là mô tả dữ liệu, chưa đối chiếu toàn bộ với mã thực thi. Có cả gói mở rộng và gói bị tắt; có dữ liệu không đồng nghĩa nhân vật đang được phép chọn.', '',
         'Tên nhân vật được nhận diện bằng mã tên có mục danh hiệu # tương ứng. Danh sách có thể không bao gồm những nhân vật không theo quy ước này. Kỹ năng được liệt kê riêng theo gói, không tự suy đoán kỹ năng thuộc nhân vật nào. Các mô tả tham chiếu bằng biểu thức Lua không phải chuỗi trực tiếp không được tự thực thi.', '']
count = 0
for p in [game / 'lang' / 'vi_VN' / 'BasaraMode.lua', *sorted((game / 'lang' / 'vi_VN' / 'Package').glob('*.lua'))]:
    source = p.read_text(encoding='utf-8-sig')
    source = re.sub(r'--\[\[.*?\]\]', '', source, flags=re.S)
    source = re.sub(r'^\s*--.*$', '', source, flags=re.M)
    pairs = [(m[1], decode(m[2])) for m in entry.finditer(source)]
    values = dict(pairs)
    desc = [(k[1:], v) for k, v in pairs if k.startswith(':')]
    if not desc:
        continue
    lines += ['## ' + p.stem, '', 'Nguồn: `' + str(p.relative_to(game)) + '`', '']
    names = [(k, v) for k, v in pairs if '#' + k in values and not k.startswith(('#', ':', '@', '~', '$', '&'))]
    if names:
        lines += ['Tên nhân vật nhận diện được: ' + '; '.join(v + ' (`' + k + '`)' for k, v in names) + '.', '']
    for key, value in desc:
        lines += ['### ' + values.get(key, key) + ' — `' + key + '`', '', value, '']
        count += 1
out = root / 'Tra-cuu-Quoc-Chien.md'
out.write_text('\n'.join(lines), encoding='utf-8')
print(f'{out}\nDescriptions: {count}; bytes: {out.stat().st_size}')
