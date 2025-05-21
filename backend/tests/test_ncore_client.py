from infrastructure.ncore_client import NCoreClient
from infrastructure.config_service import ConfigService

def test_parse_tvshow_title() -> None:
    config_service = ConfigService()
    client = NCoreClient(config_service)
    
    test_cases = [
        {
            "case":"Friday Night Lights - Tiszta szívvel foci S01-S05", 
            "result": "Friday Night Lights Tiszta szívvel foci" 
        },
        {
            "case":"Tess of the D'Urbervilles S01", 
            "result": "Tess of the D'Urbervilles"
        },
        {
            "case":"Tess.of.the.D'Urbervilles.2008.S01.BDRip.x264.Hun-BNR", 
            "result": "Tess of the D'Urbervilles"
        },
        {
            "case":"A tisztaság ára S01", 
            "result": "A tisztaság ára"
        },
        {
            "case":"Tiszta bűn S01", 
            "result": "Tiszta bűn"
        },
        {
            "case":"Sparking.Joy.S01.NF.WEBRip.x264.HUN-FULCRUM", 
            "result": "Sparking Joy"
        },
        {
            "case":"Egyiptom tisztázatlan aktái S01", 
            "result": "Egyiptom tisztázatlan aktái"
        },
        {
            "case":"Mao Mao - Tiszta Szív hősei S01 576p", 
            "result": "Mao Mao Tiszta Szív hősei"
        },
        {
            "case":"Piszkos pénz, tiszta szerelem S01", 
            "result": "Piszkos pénz, tiszta szerelem"
        },
        {
            "case":"Rossella - Egy tiszta szívű asszony S01 ", 
            "result": "Rossella Egy tiszta szívű asszony"
        },
        {
            "case":"Tiszta Hawaii S01", 
            "result": "Tiszta Hawaii"
        },
        {
            "case":"Friday.Night.Lights.S02.HUN.DVDRip.XviD-HSF", 
            "result": "Friday Night Lights"
        },
        {
            "case":"This.Fool.S02.1080p.WEB.h264-ETHEL", 
            "result": "This Fool"
        },
        {
            "case":"Pure.S01.1080p.AMZN.WEB-DL.DDP5.1.H.264.Hun-ARROW", 
            "result": "Pure"
        },
        {
            "case":"Tabula.Rasa.S01.1080p.NF.WEB-DL.DD5.1.x264.Hun-ARROW", 
            "result": "Tabula Rasa"
        },
        {
            "case":"Spotless.S01.REPACK.1080p.DRTE.WEB-DL.AAC2.0.H.264.Hun-ARROW", 
            "result": "Spotless"
        },
        {
            "case":"Horizon.S54E01.Clean.Eating.The.Dirty.Truth.1080p.DAVI.WEB-DL.AAC2.0.H264.HuN.EnG-B9R", 
            "result": "Horizon Clean Eating The Dirty Truth"
        },
        {
            "case":"White.Famous.S01.720p.SKST.WEB-DL.DD+2.0.H.264.HUN-SLN", 
            "result": "White Famous"
        },
        {
            "case":"Pandora.2019.S01.MiXED.x264-MiXGROUP", 
            "result": "Pandora"
        },
        {
            "case":"Pandora.2019.S02.WEB.h264-BAE", 
            "result": "Pandora"
        },
        {
            "case":"Pandora of the Crimson Shell S01 720p", 
            "result": "Pandora of the Crimson Shell"
        },
        {
            "case":"Pandora Hearts S01 720p", 
            "result": "Pandora Hearts"
        },
        {
            "case":"Bevándorlók Ausztráliában S01", 
            "result": "Bevándorlók Ausztráliában"
        },
        {
            "case":"Bevándorlók Ausztráliában S01 1080p", 
            "result": "Bevándorlók Ausztráliában"
        },
        {
            "case":"Andor.S02.DSNP.WEBRiP.AAC2.0.x264.HuN.EnG-B9R", 
            "result": "Andor"
        },
        {
            "case":"Bandidos.S01.2024.NF.WEBRiP.AAC2.0.x264.HuN.SpA-B9R", 
            "result": "Bandidos"
        },
        {
            "case":"Bandidos.S02.1080p.NF.WEB-DL.DV.HDR.DDP5.1.Atmos.H.265.HUN-FULCRUM", 
            "result": "Bandidos"
        },
        {
            "case":"Alexander.The.Making.of.a.God.S01.480p.NF.WEB-DL.DD+5.1.Atmos.H.264.Hun-ARROW", 
            "result": "Alexander The Making of a God"
        },
        {
            "case":"Star.Wars.Andor.S01.HS.WEBRip.x264.HUN.ENG-FULCRUM", 
            "result": "Star Wars Andor"
        },
        {
            "case":"Rocklexikon - Benkó Sándor", 
            "result": "Rocklexikon Benkó Sándor"
        },
        {
            "case":"Beforeigners.S02.HMAX.WEBRip.x264.HUN.NOR-FULCRUM", 
            "result": "Beforeigners"
        },
        {
            "case":"Sandor.Matyas.1979.S01.Read.Nfo.ReTaiL.DVDRip.x264.Hun-eStone", 
            "result": "Sandor Matyas"
        },
        {
            "case":"Vándorlás a természetben S01", 
            "result": "Vándorlás a természetben"
        },
        {
            "case":"Beforeigners.S01.WEB-DLRip.x264.HUN-Teko", 
            "result": "Beforeigners"
        },
        {
            "case":"Andor.S01E00.A.Disney.Day.Special.Look.1080p.WEB.h264-KOGi", 
            "result": "Andor A Disney Day Special Look"
        },
        {
            "case":"Időbevándorlók S01 720p", 
            "result": "Időbevándorlók"
        },
        {
            "case":"Star.Wars.Andor.S02.2160p.APPS.WEB-DL.DDP.Atmos.5.1.H.265.HuN-GOODWILL", 
            "result": "Star Wars Andor"
        },
        {
            "case":"Star.Wars.Andor.S02E01.2160p.APPS.WEB-DL.DDP.Atmos.5.1.H.265.HuN-GOODWILL", 
            "result": "Star Wars Andor"
        },
        {
            "case":"Andor.S02.1080p.DSNP.WEB-DL.DDP5.1.Atmos.DV.HDR.H265.HuN.EnG-B9R", 
            "result": "Andor"
        },
    ]
    
    for test_case in test_cases:
        assert client.parse_tvshow_title(test_case["case"]) == test_case["result"]