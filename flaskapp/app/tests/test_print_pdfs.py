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

    def test_print_pdf_aih_sus_with_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_aih_sus_with_extra_query)
        assert type(result['printPdf_AihSus']['base64Pdf']) == 'string'

    def test_print_pdf_aih_sus_without_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_aih_sus_without_extra_query)
        assert type(result['printPdf_AihSus']['base64Pdf']) == 'string'
    
    def test_print_pdf_ficha_internamento_with_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_ficha_internamento_with_extra_query)
        assert type(result['printPdf_FolhaInternamento']['base64Pdf']) == 'string'

    def test_print_pdf_ficha_internamento_without_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_ficha_internamento_without_extra_query)
        assert type(result['printPdf_FolhaInternamento']['base64Pdf']) == 'string'
    
    def test_print_pdf_relatorio_alta_with_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_relatorio_alta_with_extra_query)
        assert type(result['printPdf_RelatorioAlta']['base64Pdf']) == 'string'

    def test_print_pdf_relatorio_alta_without_extra(self, auth_client):
        result = auth_client.execute(self.print_pdf_relatorio_alta_without_extra_query)
        assert type(result['printPdf_RelatorioAlta']['base64Pdf']) == 'string'

    def test_print_pdf_folha_prescricao_with_extra(self, auth_client):
                
        timestamp_interval = get_default_timestamp_interval()

        params = {
            'startDatetimeISOString': timestamp_interval['start_datetime_ISO_string'], 
            'endingDatetimeISOString': timestamp_interval['ending_datetime_ISO_string']
        }

        result = auth_client.execute(self.print_pdf_folha_prescricao_with_extra_query, variable_values=params)
        assert type(result['printPdf_FolhaPrescricao']['base64Pdf']) == 'string'
