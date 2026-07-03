#!/usr/bin/env python3
"""Push List Interativo — DAENG ASU Jundiaí (26001)
Gera: HTML interativo + Excel banco de dados
"""
import json, os, base64, io
from pathlib import Path

try:
    from PIL import Image as PILImage
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    import openpyxl
    from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
    HAS_XL = True
except ImportError:
    HAS_XL = False

UPLOAD_DIR = "/root/.claude/uploads/001b7fb0-8857-54b0-9eb5-28053bfc3f61"
OUTPUT_DIR = "/home/user/meu-planejamento/projetos/OTZ_ASU_JUNDIAI/push_list"

# ─── DADOS DOS LOCAIS ────────────────────────────────────────────────────────
# area_group = agrupa 11+11b+11c em uma só área no dashboard
# data = data do levantamento de campo
# 5S sempre último em cada lista de serviços

AREAS = [
  {
    "num":"01","nome":"Junção ASU × CDC",
    "area_group":"Junção ASU × CDC",
    "gps":"23.1710S / 46.9501W","horario":"15:14","data":"02/07/2026",
    "endereco":"9600 Av. Pref. Luís Latorre, Setor Industrial, Jundiaí/SP",
    "fotos":["0dce6895-1001308572.jpg"],
    "servicos":[
      ("Macrodrenagem","Desforma da Escada 1"),
      ("Macrodrenagem","Recolocação da canaleta na perna da escada"),
      ("Macrodrenagem","Acabamento final da superfície da escada (nata de cimento)"),
      ("Terraplanagem","Recomposição do talude / recompactação do solo próximo à Escada 1"),
      ("Plantio de Grama","Plantio de grama na região da Escada 1"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"02","nome":"Canaleta — Escada 1",
    "area_group":"Canaleta — Escada 1",
    "gps":"23.1710S / 46.9501W","horario":"15:16","data":"02/07/2026",
    "endereco":"9600 Av. Pref. Luís Latorre, Setor Industrial, Jundiaí/SP",
    "fotos":["f46133ce-1001308573.jpg"],
    "servicos":[
      ("Macrodrenagem","Recomposição do solo e compactação na região da canaleta de interligação"),
      ("Macrodrenagem","Corte da crista do talude para padronização da perna da calha"),
      ("Plantio de Grama","Plantio de grama da base até a crista do talude"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"03","nome":"Talude / Perna / Platô — Portaria Provisória",
    "area_group":"Talude / Perna / Platô — Portaria Provisória",
    "gps":"23.1706S / 46.9497W","horario":"15:34","data":"02/07/2026",
    "endereco":"9600 Av. Pref. Luís Latorre, Setor Industrial, Jundiaí/SP",
    "fotos":["ee4ec5be-1001308585.jpg"],
    "servicos":[
      ("Macrodrenagem","Recomposição do talude / compactação do platô"),
      ("Macrodrenagem","Replantio de grama no talude (trecho com lacunas de solo exposto)"),
      ("Macrodrenagem","Acerto do terreno superficial da perna"),
      ("Macrodrenagem","Acerto do terreno superficial do platô"),
      ("Macrodrenagem","Aterrar e compactar as laterais da canaleta da perna"),
      ("Macrodrenagem","Rejuntamento com argamassa mista (traço 1:3) nas canaletas"),
      ("Macrodrenagem","Recolocação da placa de obra"),
      ("Macrodrenagem","Remoção do excedente de terra do platô"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"04","nome":"Área Perimetral da Escada 2",
    "area_group":"Área Perimetral da Escada 2",
    "gps":"23.1703S / 46.9492W","horario":"15:51","data":"02/07/2026",
    "endereco":"2045 Rod. Dom Gabriel Paulino Bueno Couto, Chácara Terra Nova, Jundiaí/SP",
    "fotos":["cbac03ca-1001308613.jpg"],
    "servicos":[
      ("Terraplanagem","Acerto e aterro no platô abaixo da berma (laterais da Escada 2) com compactação"),
      ("Macrodrenagem","Rejuntamento (traço 1:3) na canaleta da berma + compactação das laterais"),
      ("Macrodrenagem","Recomposição do talude / recompactação do solo em relação ao platô"),
      ("Macrodrenagem","Nivelamento do platô — canaleta: aterro, compactação e cimentação (traço 1:3)"),
      ("Plantio de Grama","Replantio de grama em toda a região perimetral da Escada 2"),
      ("Plantio de Grama","Replantio de grama nas laterais da escada e das canaletas"),
      ("Geral / 5S","Remoção do excedente de terra do platô"),
      ("Geral / 5S","Remoção das estacas de madeira"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"05","nome":"Talude em Curva — Escada 2",
    "area_group":"Talude em Curva — Escada 2",
    "gps":"23.1703S / 46.9492W","horario":"15:57","data":"02/07/2026",
    "endereco":"9600 Av. Pref. Luís Latorre, Setor Industrial, Jundiaí/SP",
    "fotos":["d8dad6bf-1001308617.jpg","c736ad32-1001308623.jpg","98a6888a-1001308624.jpg"],
    "servicos":[
      ("Terraplanagem","Remoção das placas de grama deslocadas do talude"),
      ("Terraplanagem","Recomposição do solo e recompactação do talude"),
      ("Plantio de Grama","Replantio de grama em todo o talude em curva"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"06","nome":"Superfície da Perna — Cota 691",
    "area_group":"Superfície da Perna — Cota 691",
    "gps":"23.1703S / 46.9492W","horario":"16:00","data":"02/07/2026",
    "endereco":"9600 Av. Pref. Luís Latorre, Setor Industrial, Jundiaí/SP",
    "fotos":["bd51de41-1001308618.jpg","37409c2b-1001308619.jpg"],
    "servicos":[
      ("Macrodrenagem / 5S","Remoção de todo o solo excedente das atividades de macrodrenagem da perna"),
      ("Macrodrenagem / 5S","Remoção das sobras de canaleta e demais materiais residuais"),
      ("Geral / 5S","Organização e limpeza geral da área da perna (cota 691)"),
    ],
  },
  {
    "num":"07","nome":"Talude do Platô — Frente à Bacia",
    "area_group":"Talude do Platô — Frente à Bacia",
    "gps":"23.1702S / 46.9491W","horario":"16:06","data":"02/07/2026",
    "endereco":"9450–9600 Av. Pref. Luís Latorre, Setor Industrial, Jundiaí/SP",
    "fotos":["cb7d3a33-1001308635.jpg","840e9892-1001308642.jpg"],
    "servicos":[
      ("Plantio de Grama","Replantio de toda a grama no talude do platô em frente à bacia"),
      ("Geral / 5S","Remoção do entulho das canaletas"),
      ("Geral / 5S","Remoção de madeira"),
      ("Geral / 5S","Remoção de grama excedente e limpeza geral da área"),
    ],
  },
  {
    "num":"08","nome":"Escada 3 — Bacia de Contenção",
    "area_group":"Escada 3 — Bacia de Contenção",
    "gps":"23.1702S / 46.9483W","horario":"16:14","data":"02/07/2026",
    "endereco":"1680 Rua Emílio Antonon / 120 Rua Nancy Carlota Netto, Chácara Aeroporto, Jundiaí/SP",
    "fotos":["38482029-1001308650.jpg","f7549f10-1001308651.jpg","7d5f4cae-1001308652.jpg","8f08fbcf-1001308653.jpg"],
    "servicos":[
      ("Macrodrenagem","Desforma da Escada 3"),
      ("Macrodrenagem","Reaterro com compactação das faces laterais da Escada 3"),
      ("Macrodrenagem","Nivelamento com aterro na parte frontal da escada em relação à rua"),
      ("Macrodrenagem","Aplicação de argamassa superficial de regularização da Escada 3"),
      ("Plantio de Grama","Recomposição de grama nas áreas adjacentes à Escada 3"),
      ("Geral / 5S","Limpeza geral e remoção de entulho e resíduos de concretagem"),
    ],
  },
  {
    "num":"09","nome":"Canaleta da Berma — Curva da Bacia (Escada 3)",
    "area_group":"Canaleta da Berma — Curva da Bacia",
    "gps":"23.1703S / 46.9483W","horario":"16:17","data":"02/07/2026",
    "endereco":"1680 Rua Emílio Antonon / 2067 Av. Pref. Luís Latorre, Chácara Aeroporto, Jundiaí/SP",
    "fotos":["8997db98-1001308654.jpg","a393ade5-1001308655.jpg"],
    "servicos":[
      ("Macrodrenagem","Remoção das canaletas da berma instaladas com problema de nivelamento"),
      ("Macrodrenagem","Nivelamento superficial da base da vala da berma"),
      ("Macrodrenagem","Acerto do nível e compactação da perna em relação à canaleta"),
      ("Macrodrenagem","Reinstalação das canaletas da berma com nivelamento correto"),
      ("Macrodrenagem","Impermeabilização interna das canaletas"),
      ("Macrodrenagem","Aplicação de argamassa de regularização (traço 1:3) nas canaletas"),
      ("Geral / 5S","Limpeza geral e remoção de entulho e resíduos da vala"),
    ],
  },
  {
    "num":"10","nome":"Talude da Bacia — Curva (Escada 3)",
    "area_group":"Talude da Bacia — Curva (Escada 3)",
    "gps":"23.1703S / 46.9483W","horario":"16:21","data":"02/07/2026",
    "endereco":"1680 Rua Emílio Antonon, Chácara Aeroporto, Jundiaí/SP",
    "fotos":["27b3328c-1001308656.jpg","64e95537-1001308657.jpg","b739367c-1001308658.jpg"],
    "servicos":[
      ("Plantio de Grama","Remoção das gramas mal instaladas e deslocadas do talude"),
      ("Terraplanagem","Nivelamento e compactação do solo do talude"),
      ("Plantio de Grama","Replantio de grama em todo o talude da curva da bacia"),
      ("Geral / 5S","Remoção de lona e resíduos do talude; limpeza geral da área"),
    ],
  },
  {
    # 11 + 11b + 11c FUNDIDOS — mesma área, 12 fotos
    "num":"11","nome":"Berma Externa — Acompanhamento da Rua",
    "area_group":"Berma Externa — Acompanhamento da Rua",
    "gps":"23.1702–1715S / 46.9479–9483W","horario":"16:25–16:30","data":"02/07/2026",
    "endereco":"982 Av. Antonieta Piva Barranqueiros / 120 R. Nancy Carlota Netto, Setor Industrial / Pq. Res. Eloy Chaves, Jundiaí/SP",
    "fotos":[
      "c8236fab-1001308670.jpg","eafa0b33-1001308671.jpg",
      "3108b587-1001308672.jpg","0ce7bdaa-1001308679.jpg",
      "bcb014dd-1001308680.jpg","f349934a-1001308681.jpg",
      "ae810a7b-1001308682.jpg","1ce90304-1001308688.jpg",
      "3bf04eef-1001308690.jpg","1a6375af-1001308691.jpg",
      "9f14ec2e-1001308697.jpg","c504e614-1001308703.jpg",
    ],
    "servicos":[
      ("Macrodrenagem","Reaterro na face lateral da canaleta de 50cm"),
      ("Macrodrenagem","Recompactação do solo nas laterais da canaleta"),
      ("Macrodrenagem","Limpeza interna da canaleta (remoção de sedimento acumulado)"),
      ("Macrodrenagem","Aplicação de argamassa de regularização (traço 1:3) nas juntas"),
      ("Macrodrenagem","Acerto no nivelamento da crista da perna"),
      ("Macrodrenagem","Remoção da grama sobre pontos de subsidência e buracos na perna"),
      ("Macrodrenagem","Recomposição do solo e nivelamento nos pontos de buraco/cavidade"),
      ("Macrodrenagem","Compactação do solo nos pontos recompostos"),
      ("Macrodrenagem","Replantio de grama na perna e berma externa"),
      ("Macrodrenagem / 5S","Remoção do excedente de terra da berma"),
      ("Geral / 5S","Limpeza geral e organização da área"),
    ],
  },
  {
    "num":"12","nome":"Transição Perna × Platô — Final do Talude",
    "area_group":"Transição Perna × Platô — Final do Talude",
    "gps":"23.1717S / 46.9482W","horario":"16:37","data":"02/07/2026",
    "endereco":"11010 Rod. Dom Gabriel Paulino Bueno Couto, Medeiros, Jundiaí/SP",
    "fotos":["a3f56521-1001308704.jpg","106c1353-1001308705.jpg"],
    "servicos":[
      ("Terraplanagem","Corte do aterro"),
      ("Terraplanagem","Nivelamento do solo"),
      ("Terraplanagem","Compactação do solo"),
      ("Plantio de Grama","Plantio de grama"),
      ("Terraplanagem","Remoção de excedente de materiais"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"13","nome":"Platô — Área de Tancagem",
    "area_group":"Platô — Área de Tancagem",
    "gps":"23.1718S / 46.9481–9482W","horario":"16:42","data":"02/07/2026",
    "endereco":"1680 Rua Emílio Antonon, Chácara Aeroporto, Jundiaí/SP",
    "fotos":["76a9d794-1001308709.jpg","7f48bd14-1001308710.jpg","36220157-1001308711.jpg"],
    "servicos":[
      ("Terraplanagem","Aplicação de água com caminhão pipa"),
      ("Terraplanagem","Nivelamento superficial da superfície"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"14","nome":"Talude do Fundo da Obra",
    "area_group":"Talude do Fundo da Obra",
    "gps":"23.1721–1722S / 46.9480W","horario":"16:45","data":"02/07/2026",
    "endereco":"1680 Rua Emílio Antonon / 11010 Rod. Dom Gabriel Paulino Bueno Couto, Medeiros, Jundiaí/SP",
    "fotos":["f26293ac-1001308715.jpg","cfb019ad-1001308716.jpg","c7b1c31f-1001308717.jpg","c2fe493a-1001308720.jpg"],
    "servicos":[
      ("Plantio de Grama","Realinhamento da grama"),
      ("Plantio de Grama","Plantio de grama no pé do talude"),
      ("Plantio de Grama","Remoção de gramas mal instaladas"),
      ("Terraplanagem","Nivelamento do solo"),
      ("Plantio de Grama","Replantio das gramas mal instaladas"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"15","nome":"Platô — Frente ao Prédio Administrativo",
    "area_group":"Platô — Frente ao Prédio Administrativo",
    "gps":"23.1721S / 46.9488W","horario":"16:51","data":"02/07/2026",
    "endereco":"11010 Rod. Dom Gabriel Paulino Bueno Couto, Medeiros, Jundiaí/SP",
    "fotos":["7587ac67-1001308725.jpg","03e95a95-1001308726.jpg","c133effc-1001308727.jpg","a72461ba-1001308728.jpg"],
    "servicos":[
      ("Terraplanagem","Remoção de materiais espalhados"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
  {
    "num":"16","nome":"Platôr Central",
    "area_group":"Platôr Central",
    "gps":"23.1712S / 46.9491W — 23.1710S / 46.9494W","horario":"09:36","data":"03/07/2026",
    "endereco":"11010 Rod. Dom Gabriel Paulino Bueno Couto + 9450 Av. Pref. Luís Latorre, Medeiros / Setor Industrial, Jundiaí/SP",
    "fotos":[],  # fotos enviadas inline — não disponíveis como arquivo
    "servicos":[
      ("Macrodrenagem","Remoção de Canaletas"),
      ("Terraplanagem","Regularização e adensamento do Platôr Central"),
      ("Geral / 5S","Limpeza geral e reorganização da área"),
    ],
  },
]

# ─── FOTO ENCODING ────────────────────────────────────────────────────────────

def encode_photo(filename, max_dim=700, quality=65):
    if not filename:
        return ""
    path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(path):
        return ""
    try:
        if HAS_PIL:
            img = PILImage.open(path).convert("RGB")
            w, h = img.size
            if max(w, h) > max_dim:
                r = max_dim / max(w, h)
                img = img.resize((int(w*r), int(h*r)), PILImage.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, "JPEG", quality=quality, optimize=True)
            data = buf.getvalue()
        else:
            with open(path, "rb") as f:
                data = f.read()
        return "data:image/jpeg;base64," + base64.b64encode(data).decode()
    except Exception as e:
        print(f"  WARN: foto {filename}: {e}")
        return ""

# ─── BUILD PAYLOAD ────────────────────────────────────────────────────────────

def build_payload():
    cards = []
    card_id = 0

    for loc in AREAS:
        fotos = loc["fotos"]
        n_fotos = len(fotos)
        area_group = loc.get("area_group", loc["nome"])

        if n_fotos > 0:
            for fi, foto in enumerate(fotos):
                card_id += 1
                print(f"  Foto {card_id}: {foto[:20]}...", flush=True)
                atividades = [
                    {"id":ai+1,"disciplina":disc,"descricao":desc,
                     "peso":1,"status":"Pendente","previsao":"","conclusao":""}
                    for ai,(disc,desc) in enumerate(loc["servicos"])
                ]
                cards.append({
                    "id": card_id,
                    "area": area_group,
                    "local_num": loc["num"],
                    "local_nome": loc["nome"],
                    "foto_idx": fi+1,
                    "foto_total": n_fotos,
                    "foto_file": foto,
                    "foto_b64": encode_photo(foto),
                    "data_levantamento": loc.get("data","02/07/2026"),
                    "gps": loc["gps"],
                    "endereco": loc["endereco"],
                    "atividades": atividades,
                    "sem_foto": False,
                })
        else:
            card_id += 1
            atividades = [
                {"id":ai+1,"disciplina":disc,"descricao":desc,
                 "peso":1,"status":"Pendente","previsao":"","conclusao":""}
                for ai,(disc,desc) in enumerate(loc["servicos"])
            ]
            cards.append({
                "id": card_id,
                "area": area_group,
                "local_num": loc["num"],
                "local_nome": loc["nome"],
                "foto_idx": 1,
                "foto_total": 0,
                "foto_file": "",
                "foto_b64": "",
                "data_levantamento": loc.get("data","02/07/2026"),
                "gps": loc["gps"],
                "endereco": loc["endereco"],
                "atividades": atividades,
                "sem_foto": True,
            })

    total_ativ = sum(len(c["atividades"]) for c in cards)
    areas_uniq = list(dict.fromkeys(c["area"] for c in cards))  # preserves order

    meta = {
        "projeto":"ASU Jundiaí (26001)",
        "contratante":"Messer Gases Ltda",
        "contratada":"Andrade e Rocha (DAENG)",
        "gerenciadora":"OTZ Engenharia — GPLAN",
        "ref":"CLM-216",
        "data_levantamento":"02/07/2026",
        "data_complemento":"03/07/2026",
        "elaborado_por":"Caio Sergio Bento da Silva & Ilson dos Santos Azevedo",
        "total_cards": len(cards),
        "total_atividades": total_ativ,
        "total_areas": len(areas_uniq),
        "areas": areas_uniq,
    }
    return {"meta": meta, "cards": cards}

# ─── GERA EXCEL ──────────────────────────────────────────────────────────────

def generate_excel(payload, out_path):
    if not HAS_XL:
        print("openpyxl não disponível — Excel ignorado")
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "PUSH LIST DAENG"

    NAV   = "0A1628"
    CYAN  = "00BCD4"
    AMBER = "FFC107"
    GREEN = "4CAF50"
    LGRAY = "D9E1EA"
    WHITE = "FFFFFF"

    def hfill(code): return PatternFill("solid", fgColor=code)
    def hfont(bold=False,color="000000",sz=10): return Font(bold=bold,color=color,size=sz,name="Calibri")
    def halign(h="center",v="center",wrap=False): return Alignment(horizontal=h,vertical=v,wrap_text=wrap)

    # Title row
    ws.merge_cells("A1:L1")
    ws["A1"] = "PUSH LIST — SERVIÇOS DAENG | ASU JUNDIAÍ (26001) | OTZ Engenharia × Messer Gases for Life"
    ws["A1"].fill = hfill(NAV); ws["A1"].font = hfont(True,"FFFFFF",13); ws["A1"].alignment = halign()
    ws.row_dimensions[1].height = 28

    # Meta row
    ws.merge_cells("A2:L2")
    m = payload["meta"]
    ws["A2"] = (f"Ref: {m['ref']}  |  Contratada: {m['contratada']}  |  "
                f"Gerenciadora: {m['gerenciadora']}  |  Levantamento: {m['data_levantamento']}"
                f"  |  Elaborado por: {m['elaborado_por']}")
    ws["A2"].fill = hfill("1E3A5F"); ws["A2"].font = hfont(False,"CADEED",9)
    ws["A2"].alignment = halign()
    ws.row_dimensions[2].height = 18

    # Headers
    headers = ["ID","Área","Local Nº","Nome do Local","Foto Idx",
               "Nº Atividade","Disciplina","Atividade / Descrição",
               "Peso","Status","Previsão Conclusão","Data Conclusão Real"]
    widths   = [6,32,8,32,8,10,20,55,6,15,18,18]
    for col, (h, w) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=h)
        cell.fill = hfill(CYAN); cell.font = hfont(True,"0A1628",10)
        cell.alignment = halign(wrap=True)
        ws.column_dimensions[cell.column_letter].width = w
    ws.row_dimensions[3].height = 22

    # Data rows
    row = 4
    status_colors = {"Pendente":"F8D7DA","Em Execução":"FFF3CD","Concluído":"D4EDDA"}
    for card in payload["cards"]:
        for atv in card["atividades"]:
            cells = [
                card["id"], card["area"], card["local_num"], card["local_nome"],
                f"F{card['foto_idx']:02d}/{card['foto_total']:02d}" if card["foto_total"] else "S/F",
                atv["id"], atv["disciplina"], atv["descricao"],
                atv["peso"], atv["status"], atv["previsao"], atv["conclusao"],
            ]
            sc = status_colors.get(atv["status"], WHITE)
            for col, val in enumerate(cells, 1):
                cell = ws.cell(row=row, column=col, value=val)
                cell.fill = hfill(sc if col >= 10 else (LGRAY if row%2==0 else WHITE))
                cell.font = hfont(sz=9)
                cell.alignment = halign("left","center",True)
            row += 1

    # Freeze + autofilter
    ws.freeze_panes = "A4"
    ws.auto_filter.ref = f"A3:L{row-1}"

    # Summary sheet
    ws2 = wb.create_sheet("RESUMO")
    ws2["A1"] = "RESUMO POR ÁREA"
    ws2["A1"].fill = hfill(NAV); ws2["A1"].font = hfont(True,"FFFFFF",12)
    ws2.merge_cells("A1:E1")
    ws2.row_dimensions[1].height = 24

    ws2["A2"]="Área"; ws2["B2"]="Fotos"; ws2["C2"]="Atividades"; ws2["D2"]="Pendentes"; ws2["E2"]="Concluídas"
    for cell in [ws2["A2"],ws2["B2"],ws2["C2"],ws2["D2"],ws2["E2"]]:
        cell.fill = hfill(CYAN); cell.font = hfont(True,"0A1628")

    area_data = {}
    for card in payload["cards"]:
        a = card["area"]
        if a not in area_data:
            area_data[a] = {"fotos":0,"ativ":0,"pend":0,"conc":0}
        area_data[a]["fotos"] += 1
        for atv in card["atividades"]:
            area_data[a]["ativ"] += 1
            if atv["status"] == "Pendente":    area_data[a]["pend"] += 1
            if atv["status"] == "Concluído":   area_data[a]["conc"] += 1

    for r2, (area, d) in enumerate(area_data.items(), 3):
        ws2.cell(r2,1,area).alignment = halign("left","center",True)
        ws2.cell(r2,2,d["fotos"])
        ws2.cell(r2,3,d["ativ"])
        ws2.cell(r2,4,d["pend"])
        ws2.cell(r2,5,d["conc"])
        bg = LGRAY if r2%2==0 else WHITE
        for c in range(1,6):
            ws2.cell(r2,c).fill = hfill(bg)

    ws2.column_dimensions["A"].width = 42
    for col in ["B","C","D","E"]:
        ws2.column_dimensions[col].width = 14

    wb.save(out_path)
    print(f"Excel salvo: {out_path}")

# ─── HTML ─────────────────────────────────────────────────────────────────────

CSS = """
:root{
  --bg:#0A1628;--surface:#0F2040;--surface2:#132850;--border:#1E3A5F;
  --accent:#00BCD4;--accent2:#00E676;--warn:#FFC107;--danger:#F44336;
  --text:#E8EDF3;--text-dim:#7EB8D4;--text-muted:#4A7A9B;
  --nav:#051020;--card-h:40px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',Arial,sans-serif;font-size:13px}
a{color:var(--accent)}

/* ── HEADER ── */
#page-header{
  background:linear-gradient(135deg,var(--nav) 0%,#0A2040 60%,#0D2D55 100%);
  border-bottom:2px solid var(--accent);
  padding:14px 24px;display:flex;align-items:center;justify-content:space-between;
  position:sticky;top:0;z-index:100;
}
.logo-block{display:flex;align-items:center;gap:16px}
.logo-box{
  background:var(--surface2);border:1px solid var(--border);border-radius:6px;
  padding:6px 14px;font-size:11px;font-weight:700;color:var(--accent);
  letter-spacing:1px;text-align:center;line-height:1.4;
}
.header-title h1{font-size:18px;font-weight:700;color:var(--text);letter-spacing:.5px}
.header-title p{font-size:10px;color:var(--text-muted);margin-top:2px}

/* ── DASHBOARD ── */
#dashboard{background:var(--surface);border-bottom:1px solid var(--border);padding:20px 24px}
.dash-grid{display:grid;grid-template-columns:180px repeat(4,1fr) 2fr;gap:16px;align-items:center}
.gauge-wrap{display:flex;flex-direction:column;align-items:center}
.gauge-wrap svg{width:160px;height:96px}
.gauge-label{font-size:10px;color:var(--text-muted);margin-top:4px;text-align:center}

.kpi-card{
  background:var(--surface2);border:1px solid var(--border);border-radius:8px;
  padding:14px 16px;text-align:center;
}
.kpi-num{font-size:28px;font-weight:700;color:var(--accent)}
.kpi-num.done{color:var(--accent2)}
.kpi-num.prog{color:var(--warn)}
.kpi-num.pend{color:var(--text-dim)}
.kpi-label{font-size:10px;color:var(--text-muted);margin-top:4px;text-transform:uppercase;letter-spacing:.8px}

.disc-bars{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:12px 16px}
.disc-bars h4{font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.8px;margin-bottom:10px}
.dbar-row{display:flex;align-items:center;gap:8px;margin-bottom:7px}
.dbar-label{font-size:10px;color:var(--text-dim);width:130px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dbar-track{flex:1;height:8px;background:var(--border);border-radius:4px;overflow:hidden}
.dbar-fill{height:100%;border-radius:4px;transition:width .8s ease}
.dbar-count{font-size:10px;color:var(--text-muted);width:50px;text-align:right}

/* ── FILTERS ── */
#filters{
  background:var(--nav);border-bottom:1px solid var(--border);
  padding:12px 24px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;
  position:sticky;top:61px;z-index:90;
}
#filters label{font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.7px}
#filters select,#filters input{
  background:var(--surface2);color:var(--text);border:1px solid var(--border);
  border-radius:5px;padding:6px 10px;font-size:12px;outline:none;
}
#filters select:focus,#filters input:focus{border-color:var(--accent)}
#filters input{width:200px}
#count-label{margin-left:auto;font-size:11px;color:var(--text-muted)}

/* ── CARDS GRID ── */
#cards-wrap{padding:20px 24px}
#cards-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:18px}

.card{
  background:var(--surface);border:1px solid var(--border);border-radius:10px;
  overflow:hidden;display:flex;flex-direction:column;transition:box-shadow .2s;
}
.card:hover{box-shadow:0 4px 20px rgba(0,188,212,.15);border-color:var(--accent)}

.card-head{
  background:linear-gradient(90deg,#0D2D55,#0A1E42);
  padding:10px 14px;display:flex;justify-content:space-between;align-items:flex-start;
  border-bottom:1px solid var(--border);
}
.card-area{font-size:12px;font-weight:700;color:var(--accent);line-height:1.3;max-width:70%}
.card-meta{font-size:10px;color:var(--text-muted);text-align:right;white-space:nowrap}
.card-local{font-size:10px;color:var(--text-dim);margin-top:3px}

.card-photo{
  width:100%;aspect-ratio:4/3;overflow:hidden;background:#050E1C;
  display:flex;align-items:center;justify-content:center;
  border-bottom:1px solid var(--border);
}
.card-photo img{width:100%;height:100%;object-fit:cover}
.no-photo{
  text-align:center;color:var(--text-muted);font-size:11px;padding:20px;
  display:flex;flex-direction:column;align-items:center;gap:8px;
}
.no-photo svg{opacity:.4}

.card-activities{overflow-x:auto}
.atv-table{width:100%;border-collapse:collapse;font-size:11px}
.atv-table th{
  background:#0D2040;color:var(--text-muted);font-weight:600;
  padding:6px 8px;text-align:left;white-space:nowrap;font-size:10px;
  border-bottom:1px solid var(--border);
}
.atv-table td{padding:5px 8px;border-bottom:1px solid #0D1E33;vertical-align:middle}
.atv-table tr:last-child td{border-bottom:none}
.atv-table tr:hover td{background:rgba(0,188,212,.05)}

.disc-badge{
  display:inline-block;padding:2px 6px;border-radius:3px;font-size:9.5px;
  font-weight:600;white-space:nowrap;
}
.disc-macro{background:#003B4A;color:#00BCD4}
.disc-terra{background:#3D2E00;color:#FFC107}
.disc-grama{background:#1B3A1B;color:#66BB6A}
.disc-5s   {background:#2A1040;color:#CE93D8}

.status-dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px}
.s-pend{background:#607D8B}
.s-exec{background:#FFC107}
.s-conc{background:#00E676}

.card-footer{
  background:#080F1E;border-top:1px solid var(--border);
  padding:8px 14px;display:flex;align-items:center;gap:12px;flex-wrap:wrap;
}
.cf-weight{font-size:10px;color:var(--text-muted)}
.cf-prog{font-size:10px;font-weight:600}
.cf-badge{
  margin-left:auto;font-size:10px;font-weight:700;padding:3px 10px;border-radius:12px;
}
.cf-pend{background:#1A2E3A;color:#90A4AE}
.cf-exec{background:#3D2E00;color:#FFC107}
.cf-conc{background:#1B3A1B;color:#00E676}

/* ── FOOTER ── */
#page-footer{
  background:var(--nav);border-top:1px solid var(--border);
  padding:14px 24px;text-align:center;font-size:10px;color:var(--text-muted);
}

/* ── RESPONSIVE ── */
@media(max-width:900px){
  .dash-grid{grid-template-columns:repeat(2,1fr)}
  .gauge-wrap{grid-column:1/-1}
  #filters{top:0}
}
@media(max-width:600px){
  #cards-grid{grid-template-columns:1fr}
  .dash-grid{grid-template-columns:1fr 1fr}
}
"""

JS = r"""
const PL = window.PAYLOAD;
const meta = PL.meta;
let currentCards = [...PL.cards];

// ── DISC COLOR ──────────────────────────────────────────────────────────────
function discClass(d){
  if(d.includes('Macrodrenagem')) return 'disc-macro';
  if(d.includes('Terraplanagem')) return 'disc-terra';
  if(d.includes('Grama'))         return 'disc-grama';
  return 'disc-5s';
}
function statusClass(s){
  if(s==='Concluído')   return 's-conc';
  if(s==='Em Execução') return 's-exec';
  return 's-pend';
}
function cardBadgeClass(card){
  const n=card.atividades.length;
  const done=card.atividades.filter(a=>a.status==='Concluído').length;
  const exec=card.atividades.filter(a=>a.status==='Em Execução').length;
  if(done===n) return 'cf-conc';
  if(exec>0)   return 'cf-exec';
  return 'cf-pend';
}
function cardStatusLabel(card){
  const n=card.atividades.length;
  const done=card.atividades.filter(a=>a.status==='Concluído').length;
  const exec=card.atividades.filter(a=>a.status==='Em Execução').length;
  if(done===n) return 'Concluído';
  if(exec>0)   return 'Em Execução';
  return 'Pendente';
}

// ── GAUGE (SVG semicircle) ──────────────────────────────────────────────────
function drawGauge(pct){
  const svg = document.getElementById('gauge-svg');
  const r=70, cx=80, cy=78;
  const toRad = d => d * Math.PI/180;
  // arc from 180° to 0° (left to right along bottom)
  const x0 = cx + r*Math.cos(toRad(180)); // 10
  const y0 = cy - r*Math.sin(toRad(180)); // 78
  const x1 = cx + r*Math.cos(toRad(0));   // 150
  const y1 = cy;
  // progress endpoint
  const ang = 180 - pct/100*180;
  const xp = cx + r*Math.cos(toRad(ang));
  const yp = cy - r*Math.sin(toRad(ang));
  const lg = pct > 50 ? 1 : 0;
  svg.innerHTML =
    `<path d="M${x0},${y0} A${r},${r} 0 0,1 ${x1},${y1}"
           stroke="#1A3A5C" stroke-width="12" fill="none" stroke-linecap="round"/>
     <path d="M${x0},${y0} A${r},${r} 0 ${lg},1 ${xp.toFixed(1)},${yp.toFixed(1)}"
           stroke="#00BCD4" stroke-width="12" fill="none" stroke-linecap="round"
           style="transition:stroke-dashoffset 1s ease"/>
     <text x="${cx}" y="${cy-12}" text-anchor="middle" fill="#00BCD4"
           font-size="26" font-weight="700" font-family="Segoe UI,sans-serif">${pct}%</text>
     <text x="${cx}" y="${cy+12}" text-anchor="middle" fill="#4A7A9B"
           font-size="9" font-family="Segoe UI,sans-serif">AVANÇO GERAL</text>`;
}

// ── DASHBOARD ───────────────────────────────────────────────────────────────
function renderDashboard(cards){
  const allAtv = cards.flatMap(c=>c.atividades);
  const total  = allAtv.length;
  const done   = allAtv.filter(a=>a.status==='Concluído').length;
  const exec   = allAtv.filter(a=>a.status==='Em Execução').length;
  const pend   = allAtv.filter(a=>a.status==='Pendente').length;
  const pct    = total>0 ? Math.round(done/total*100) : 0;

  drawGauge(pct);
  document.getElementById('kpi-total').textContent = total;
  document.getElementById('kpi-done').textContent  = done;
  document.getElementById('kpi-exec').textContent  = exec;
  document.getElementById('kpi-pend').textContent  = pend;
  document.getElementById('kpi-cards').textContent = cards.length;

  // Discipline bars
  const discs = {};
  allAtv.forEach(a=>{
    const k = a.disciplina.length > 18 ? a.disciplina.slice(0,18)+'…' : a.disciplina;
    const full = a.disciplina;
    if(!discs[full]) discs[full]={label:k,total:0,done:0};
    discs[full].total++;
    if(a.status==='Concluído') discs[full].done++;
  });
  const maxDisc = Math.max(...Object.values(discs).map(d=>d.total));
  const colors = ['#00BCD4','#FFC107','#66BB6A','#CE93D8','#4DB6AC'];
  const dbars = document.getElementById('disc-bars');
  dbars.innerHTML = '';
  Object.entries(discs).forEach(([k,d],i)=>{
    const pct2 = maxDisc>0 ? d.total/maxDisc*100 : 0;
    const dPct = d.total>0 ? Math.round(d.done/d.total*100) : 0;
    dbars.innerHTML +=
      `<div class="dbar-row">
        <span class="dbar-label" title="${k}">${d.label}</span>
        <div class="dbar-track"><div class="dbar-fill" style="width:${pct2}%;background:${colors[i%colors.length]}"></div></div>
        <span class="dbar-count">${d.done}/${d.total} (${dPct}%)</span>
       </div>`;
  });
}

// ── POPULATE FILTERS ────────────────────────────────────────────────────────
function populateFilters(){
  const areas = [...new Set(PL.cards.map(c=>c.area))];
  const asel = document.getElementById('f-area');
  areas.forEach(a=>{ const o=document.createElement('option'); o.value=a; o.textContent=a; asel.appendChild(o); });

  const discs = [...new Set(PL.cards.flatMap(c=>c.atividades.map(a=>a.disciplina)))];
  const dsel = document.getElementById('f-disc');
  discs.forEach(d=>{ const o=document.createElement('option'); o.value=d; o.textContent=d; dsel.appendChild(o); });
}

// ── FILTER & RENDER ─────────────────────────────────────────────────────────
function applyFilters(){
  const area   = document.getElementById('f-area').value;
  const disc   = document.getElementById('f-disc').value;
  const status = document.getElementById('f-status').value;
  const q      = document.getElementById('f-search').value.toLowerCase();

  let filtered = PL.cards.filter(card=>{
    if(area && card.area !== area) return false;
    if(status){
      const cs = cardStatusLabel(card);
      if(cs !== status) return false;
    }
    if(disc){
      if(!card.atividades.some(a=>a.disciplina===disc)) return false;
    }
    if(q){
      const hay = (card.area+card.local_nome+card.atividades.map(a=>a.descricao).join(' ')).toLowerCase();
      if(!hay.includes(q)) return false;
    }
    return true;
  });

  renderCards(filtered);
  renderDashboard(filtered);
  document.getElementById('count-label').textContent = `${filtered.length} de ${PL.cards.length} locais`;
}

// ── RENDER CARDS ─────────────────────────────────────────────────────────────
function renderCards(cards){
  const grid = document.getElementById('cards-grid');
  grid.innerHTML = '';
  cards.forEach(card=>{
    const done = card.atividades.filter(a=>a.status==='Concluído').length;
    const n    = card.atividades.length;
    const peso = card.atividades.reduce((s,a)=>s+a.peso,0);

    const rows = card.atividades.map(a=>`
      <tr>
        <td style="color:#4A7A9B;text-align:center">${a.id}</td>
        <td><span class="disc-badge ${discClass(a.disciplina)}">${a.disciplina}</span></td>
        <td style="color:#C5D3E0">${a.descricao}</td>
        <td style="text-align:center;color:#4A7A9B">${a.peso}</td>
        <td><span class="status-dot ${statusClass(a.status)}"></span><span style="font-size:10px;color:#7EB8D4">${a.status}</span></td>
      </tr>`).join('');

    const photoEl = card.foto_b64
      ? `<img src="${card.foto_b64}" alt="Foto ${card.foto_idx}" loading="lazy">`
      : `<div class="no-photo">
           <svg width="40" height="40" viewBox="0 0 24 24" fill="#4A7A9B">
             <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
           </svg>
           <span>Foto não disponível</span>
           <span style="font-size:9px">Imagem enviada via mensagem — não armazenada como arquivo</span>
         </div>`;

    const fotoLabel = card.foto_total > 0
      ? `F${String(card.foto_idx).padStart(2,'0')}/${String(card.foto_total).padStart(2,'0')}`
      : 'S/F';

    const div = document.createElement('div');
    div.className = 'card';
    div.dataset.area = card.area;
    div.innerHTML = `
      <div class="card-head">
        <div>
          <div class="card-area">${card.area}</div>
          <div class="card-local">Local ${card.local_num} — ${card.local_nome}</div>
        </div>
        <div class="card-meta">
          <div>${fotoLabel}</div>
          <div>${card.data_levantamento}</div>
        </div>
      </div>
      <div class="card-photo">${photoEl}</div>
      <div class="card-activities">
        <table class="atv-table">
          <thead><tr>
            <th style="width:28px">#</th>
            <th style="width:120px">Disciplina</th>
            <th>Atividade</th>
            <th style="width:30px">Peso</th>
            <th style="width:90px">Status</th>
          </tr></thead>
          <tbody>${rows}</tbody>
        </table>
      </div>
      <div class="card-footer">
        <span class="cf-weight">Peso: ${peso}</span>
        <span class="cf-prog">${done}/${n} concluídas</span>
        <span class="cf-badge ${cardBadgeClass(card)}">${cardStatusLabel(card)}</span>
      </div>`;
    grid.appendChild(div);
  });
}

// ── INIT ────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', ()=>{
  populateFilters();
  renderDashboard(PL.cards);
  renderCards(PL.cards);
  document.getElementById('count-label').textContent =
    `${PL.cards.length} de ${PL.cards.length} locais`;

  ['f-area','f-disc','f-status'].forEach(id=>{
    document.getElementById(id).addEventListener('change', applyFilters);
  });
  document.getElementById('f-search').addEventListener('input', applyFilters);
  document.getElementById('btn-reset').addEventListener('click', ()=>{
    ['f-area','f-disc','f-status'].forEach(id=>{ document.getElementById(id).value=''; });
    document.getElementById('f-search').value='';
    applyFilters();
  });
});
"""


def generate_html(payload):
    data_json = json.dumps(payload, ensure_ascii=False, separators=(',', ':'))
    m = payload["meta"]
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Push List DAENG — ASU Jundiaí (26001)</title>
<style>{CSS}</style>
</head>
<body>

<header id="page-header">
  <div class="logo-block">
    <div class="logo-box">MESSER<br>GASES FOR LIFE</div>
    <div class="logo-box">OTZ<br>ENGENHARIA<br><span style="color:#7EB8D4;font-weight:400">GPLAN</span></div>
  </div>
  <div class="header-title">
    <h1>PUSH LIST — SERVIÇOS DAENG</h1>
    <p>ASU Jundiaí (26001) &nbsp;|&nbsp; Ref: {m['ref']} &nbsp;|&nbsp; Contratada: {m['contratada']} &nbsp;|&nbsp; Gerenciadora: {m['gerenciadora']}</p>
  </div>
  <div class="logo-box" style="text-align:right">
    <div style="color:#7EB8D4;font-size:9px">Levantamento</div>
    <div style="color:#E8EDF3">{m['data_levantamento']}</div>
    <div style="color:#7EB8D4;font-size:9px">{m['total_cards']} locais &nbsp;|&nbsp; {m['total_atividades']} atividades</div>
  </div>
</header>

<section id="dashboard">
  <div class="dash-grid">
    <div class="gauge-wrap">
      <svg id="gauge-svg" viewBox="0 0 160 90" xmlns="http://www.w3.org/2000/svg"></svg>
      <div class="gauge-label">% AVANÇO TOTAL<br><span style="font-size:9px;color:#1E3A5F">Atualizado pelo Excel</span></div>
    </div>
    <div class="kpi-card">
      <div class="kpi-num" id="kpi-total">—</div>
      <div class="kpi-label">Total Atividades</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-num done" id="kpi-done">—</div>
      <div class="kpi-label">Concluídas</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-num prog" id="kpi-exec">—</div>
      <div class="kpi-label">Em Execução</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-num pend" id="kpi-pend">—</div>
      <div class="kpi-label">Pendentes</div>
    </div>
    <div class="disc-bars">
      <h4>Atividades por Disciplina</h4>
      <div id="disc-bars"></div>
    </div>
  </div>
  <div style="margin-top:12px;font-size:10px;color:#1E3A5F;text-align:right">
    ℹ️ Curva-S disponível após DAENG fornecer datas de previsão de conclusão
  </div>
</section>

<section id="filters">
  <label>Área</label>
  <select id="f-area"><option value="">Todas</option></select>
  <label>Disciplina</label>
  <select id="f-disc"><option value="">Todas</option></select>
  <label>Status</label>
  <select id="f-status">
    <option value="">Todos</option>
    <option>Pendente</option>
    <option>Em Execução</option>
    <option>Concluído</option>
  </select>
  <label>Busca</label>
  <input id="f-search" type="text" placeholder="Pesquisar atividade...">
  <button id="btn-reset" style="background:#1E3A5F;color:#7EB8D4;border:1px solid #1E3A5F;border-radius:5px;padding:6px 14px;cursor:pointer;font-size:11px">Limpar</button>
  <span id="count-label" style="margin-left:auto"></span>
</section>

<div id="cards-wrap">
  <div id="cards-grid"></div>
</div>

<footer id="page-footer">
  Push List DAENG — ASU Jundiaí (26001) &nbsp;|&nbsp;
  Elaborado por: {m['elaborado_por']} &nbsp;|&nbsp;
  OTZ Engenharia × Messer Gases for Life &nbsp;|&nbsp;
  Levantamento: {m['data_levantamento']} / {m['data_complemento']} &nbsp;|&nbsp;
  Gerado automaticamente — não editar manualmente
</footer>

<script>
window.PAYLOAD = {data_json};
{JS}
</script>
</body>
</html>"""
    return html

# ─── MAIN ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Construindo payload (encodando fotos)...")
    payload = build_payload()

    print(f"\nCards: {payload['meta']['total_cards']}")
    print(f"Atividades: {payload['meta']['total_atividades']}")
    print(f"Áreas: {payload['meta']['total_areas']}")

    # Excel
    xl_path = os.path.join(OUTPUT_DIR, "DAENG_PUSH_LIST_ASU_JUNDIAI.xlsx")
    print("\nGerando Excel...")
    generate_excel(payload, xl_path)

    # HTML
    print("\nGerando HTML...")
    html = generate_html(payload)
    html_path = os.path.join(OUTPUT_DIR, "DAENG_PUSH_LIST_ASU_JUNDIAI.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    size_mb = os.path.getsize(html_path) / 1024 / 1024
    print(f"HTML salvo: {html_path} ({size_mb:.1f} MB)")
    print("\nPronto!")
