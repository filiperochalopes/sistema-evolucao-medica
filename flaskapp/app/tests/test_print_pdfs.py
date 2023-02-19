from gql import gql
from app.utils import get_default_timestamp_interval
from app.tests.conftest import get_query_from_txt


class TestPrintPdfs:
    print_pdf_aih_sus_with_extra_query = gql(get_query_from_txt('print_pdf_aih_sus_with_extra'))
    print_pdf_aih_sus_without_extra_query = gql(get_query_from_txt('print_pdf_aih_sus_without_extra'))
    print_pdf_ficha_internamento_with_extra_query = gql(get_query_from_txt('print_pdf_ficha_internamento_with_extra'))
    print_pdf_ficha_internamento_without_extra_query = gql(get_query_from_txt('print_pdf_ficha_internamento_without_extra'))
    print_pdf_relatorio_alta_with_extra_query = gql(get_query_from_txt('print_pdf_relatorio_alta_with_extra'))
    print_pdf_relatorio_alta_without_extra_query = gql(get_query_from_txt('print_pdf_relatorio_alta_without_extra'))
    print_pdf_folha_prescricao_with_extra_query = gql(get_query_from_txt('print_pdf_folha_prescricao_with_extra'))
    print_pdf_folha_prescricao_without_extra_query = gql(get_query_from_txt('print_pdf_folha_prescricao_without_extra'))
    print_pdf_folha_evolucao_without_extra_query = gql(get_query_from_txt('print_pdf_folha_evolucao_without_extra'))
    print_pdf_apac_with_extra_query = gql(get_query_from_txt('print_pdf_apac_with_extra'))
    print_pdf_balanco_hidrico_without_extra_query = gql(get_query_from_txt('print_pdf_balanco_hidrico_without_extra'))

    def test_print_pdf_aih_sus_with_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_aih_sus_with_extra_query)
        assert isinstance(result['printPdf_AihSus']['base64Pdf'], str)

    def test_print_pdf_aih_sus_without_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_aih_sus_without_extra_query)
        assert isinstance(result['printPdf_AihSus']['base64Pdf'], str)
    
    def test_print_pdf_ficha_internamento_with_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_ficha_internamento_with_extra_query)
        assert isinstance(result['printPdf_FichaInternamento']['base64Pdf'], str)

    def test_print_pdf_ficha_internamento_without_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_ficha_internamento_without_extra_query)
        assert isinstance(result['printPdf_FichaInternamento']['base64Pdf'], str)
    
    def test_print_pdf_relatorio_alta_with_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_relatorio_alta_with_extra_query)
        assert isinstance(result['printPdf_RelatorioAlta']['base64Pdf'], str)

    def test_print_pdf_relatorio_alta_without_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_relatorio_alta_without_extra_query)
        assert isinstance(result['printPdf_RelatorioAlta']['base64Pdf'], str)

    def test_print_pdf_folha_prescricao_with_extra(self, auth_client):
                
        print("======================")
        timestamp_interval = get_default_timestamp_interval()

        print("======================")
        params = {
            'startDatetimeISOString': timestamp_interval.start_datetime_ISO_string, 
            'endingDatetimeISOString': timestamp_interval.ending_datetime_ISO_string
        }

        print("======================")
        result = auth_client.execute(self.print_pdf_folha_prescricao_with_extra_query, variable_values=params)
        print(result)
        print(result.keys())
        assert isinstance(result['printPdf_FolhaPrescricao']['base64Pdf'], str)

    def test_print_pdf_folha_evolucao_without_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_folha_evolucao_without_extra_query)
        assert isinstance(result['printPdf_FolhaEvolucao']['base64Pdf'], str)

    def test_print_pdf_apac_with_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_apac_with_extra_query)
        assert isinstance(result['printPdf_Apac']['base64Pdf'], str)

    def test_print_pdf_balanco_hidrico_without_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_balanco_hidrico_without_extra_query)
        assert isinstance(result['printPdf_BalancoHidrico']['base64Pdf'], str)
        