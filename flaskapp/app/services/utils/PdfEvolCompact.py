from app.env import TEMPLATE_COMPACTED_DIRECTORY, WRITE_COMPACTED_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader
from dateutil.parser import isoparse
import datetime


class PdfEvolCompact(ReportLabCanvasUtils):
    TEMPLATE_DIRECTORY = TEMPLATE_COMPACTED_DIRECTORY
    WRITE_DIRECTORY = WRITE_COMPACTED_DIRECTORY

    def __init__(self) -> None:
        page_size_points = (842, 595)
        super().__init__(canvas_pagesize=page_size_points)
        self.can.setFont("Roboto-Condensed-Bold", 20)

    def get_output(self) -> PdfWriter:
        """Return a PdfWriter Object to output a file"""
        return super().get_output()

    def create_professional_info_text(
        self, professional: dict, date: str, nullable: bool = True
    ):
        """Create professional info string.
        Example: "Responsavel Medico {name} CRM {number}/{uf}"

        Args:
            professional (dict): Dict with professioanl info
        """

        self.validate_func_args(
            function_to_verify=self.create_professional_info_text,
            variables_to_verify={
                "professional": professional,
                "nullable": nullable,
                "date": date,
            },
        )

        # getting data
        name = professional.get("name")
        document = professional.get("document")
        category = professional.get("category")

        if not nullable:
            # if any camp can be null, the function will check all variables and return a Exception if is missing
            for camp in [name, document]:
                if camp == None:
                    raise Exception(
                        'Algum campo do profissional está faltando, o profissional precisa do nome, e documento no formato "54321/BA"'
                    )

        date_object = isoparse(date)
        str_date = str("%02d/%02d/%d %02d:%02d") % (
            date_object.day,
            date_object.month,
            date_object.year,
            date_object.hour,
            date_object.minute,
        )

        document_category = "CRM" if category.lower() == "doc" else "COREN"

        prof_info = (
            f"{str(name).strip()} {document_category} {str(document)}"
            + " Criado em: "
            + str_date
        )

        return prof_info

    def add_prescription(self, prescription: list) -> None:
        """add prescription to database

        Args:
            precription (list): list of dicts
        Returns:
            None
        """
        # verify if the type is list
        if type(prescription) != type(list()):
            raise Exception(
                'prescription deve ser uma lista'
            )
        

        CHAR_PER_LINES = 82
        DEFAULT_RECT_HEIGHT = 1
        DEFAULT_RECT_WIDTH = 528
        DEFAULT_DECREASE_Y_POS = 10
        count = 1
        yposition = 387

        for presc in prescription:
            current_text = presc['description'].strip()

            if count != 1:
                rect_y_pos = int(yposition + 11)
                self.add_rectangle(
                    pos=(17, rect_y_pos),
                    height=DEFAULT_RECT_HEIGHT,
                    width=DEFAULT_RECT_WIDTH,
                    fill=1,
                    color=(0.5215, 0.5215, 0.5215),
                )
            yposition = self.add_morelines_text(
                text=current_text,
                initial_pos=(18, yposition),
                decrease_ypos=DEFAULT_DECREASE_Y_POS,
                field_name=f"{count} Prescription",
                len_max=4032,
                char_per_lines=CHAR_PER_LINES,
                return_ypos=True,
                max_lines_amount=2,
                auto_adjust=True
            )
            if yposition <= 110:
                raise Exception(
                    "Voce chegou ao limite do documento, reduza o numero de prescricoes"
                )
            count += 1
            yposition -= DEFAULT_DECREASE_Y_POS - 3

        return None

    def get_measures_list(self, date_object: datetime, measure: dict):
        """Return measures list with the tabel order to use index

        Args:
            date_object (datetime): date object
            measure (dict): current measure

        Returns:
            _type_: _description_
        """
        created_at = str("%02d:%02d") % (date_object.hour, date_object.minute)
        cardiac_frequency = measure.get("cardiac_frequency")
        respiratory_frequency = measure.get("respiratory_frequency")
        sistolic_blood_pressure = measure.get("sistolic_blood_pressure")
        diastolic_blood_pressure = measure.get("diastolic_blood_pressure")
        glucose = measure.get("glucose")
        spO2 = measure.get("sp_o_2")
        celcius_axillary_temperature = measure.get("celcius_axillary_temperature")
        pain = measure.get("pain")
        fetal_cardiac_frequency = measure.get("fetal_cardiac_frequency")

        # Creating blood plesure
        blood_pressure = (
            str(sistolic_blood_pressure) + "/" + str(diastolic_blood_pressure)
        )

        measures_list = [
            created_at,
            spO2,
            pain,
            blood_pressure,
            cardiac_frequency,
            respiratory_frequency,
            celcius_axillary_temperature,
            glucose,
            fetal_cardiac_frequency,
        ]

        return measures_list

    def add_measures(self, measures: list) -> None:
        """Add measures to pdf

        Args:
            measures (list): list of dicts

        Returns:
            None
        """
        try:
            if measures is None:
                return None
            self.validate_func_args(
                function_to_verify=self.add_measures,
                variables_to_verify={"measures": measures},
            )

            if len(measures) > 6:
                raise Exception("You cant add more than 6 measures")

            INITIAL_Y_POS = 378
            INITIAL_X_POS = 607
            DEFAULT_DECREASE_Y_POS = 24
            DEFAULT_INCREASE_X_POS = 40
            # Add to cnavas
            global_count = 0
            y_pos = INITIAL_Y_POS
            x_pos = INITIAL_X_POS

            for m in measures:
                all_list_ypos = [INITIAL_Y_POS, 354, 329, 304, 280, 255, 230, 206, 179]
                complete_time = m.get("created_at")
                if complete_time == None:
                    raise Exception("create_at cannot be null")

                # Transform create_at to datetime object
                try:
                    date_object = isoparse(complete_time)
                except:
                    raise Exception(
                        f"A data nao corresponde ao formato ISO %Y-%m-%dT%H:%M:%S"
                    )

                measures_list = self.get_measures_list(
                    date_object=date_object, measure=m
                )

                list_ypos = []
                for value in measures_list:
                    list_ypos.append(y_pos)
                    if value == None:
                        # y_pos -= DEFAULT_DECREASE_Y_POS
                        continue

                    self.add_oneline_text(
                        text=str(value),
                        pos=(x_pos, all_list_ypos.pop(0)),
                        field_name=f"{global_count} Measure",
                        len_max=10,
                        len_min=1,
                        centralized=True,
                    )

                    # y_pos -= DEFAULT_DECREASE_Y_POS

                # Update count variables
                # y_pos = INITIAL_Y_POS
                x_pos += DEFAULT_INCREASE_X_POS

            # Add new responsible name to docs
            self.set_font("Roboto-Mono", 8)

            return None
        except Exception as error:
            raise error
        except:
            raise Exception(
                "Erro inesperado enquanto adicionava measures em folha de Evolucao"
            )

    def get_optional_data(self, patient: dict, regulation_code: str) -> None:
        optional_data = ""
        for item in [
            ["Alergias", patient.get("allergies")],
            ["Comobidades", patient.get("comorbidities")],
        ]:
            if item[1] != None:
                data = str(item[1]).replace("'", "").replace("[", "").replace("]", "")
                optional_data += f" {item[0]}: {data}"
        if regulation_code != None:
            optional_data += f" Codigo_de_Regulação: {regulation_code}"

        return optional_data
    
    def add_nursing_prescriptions(self, nursing_prescriptions):
        resting = nursing_prescriptions.get("resting")
        diet = nursing_prescriptions.get("diet")
        activities = nursing_prescriptions.get("activities")

        total_string = ""
        if resting != None and resting != "":
            total_string += f' REPOUSO: {str(resting).strip()}'
        
        if diet != None and diet != "":
            total_string += f' DIETA: {str(diet).strip()}'

        if activities != None and len(activities) > 0:
            total_string += f' ATIVIDADES:'
            for activity in activities:
                total_string += f' {activity["description"].strip()} |'

        return self.add_morelines_text(
                text=total_string,
                initial_pos=(18, 125),
                field_name="Cuidados de Enfermagem, Dieta e Atividades",
                len_max=403,
                len_min=5,
                char_per_lines=67,
                decrease_ypos=10,
                max_lines_amount=6,
                auto_adjust=True,
                bold_words=['REPOUSO:', 'DIETA:', 'ATIVIDADES:'],
                nullable=True
        )
    

    def get_pendings_text(self, pendings):
        date_object = isoparse(pendings["created_at"])
        str_date = str("%02d/%02d/%d %02d:%02d") % (
            date_object.day,
            date_object.month,
            date_object.year,
            date_object.hour,
            date_object.minute,
        )

        text = f' PENDÊNCIAS: {pendings["description"]} ({str_date})'

        return text
