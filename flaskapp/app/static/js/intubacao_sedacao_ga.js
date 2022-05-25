$(document).ready(function () {
  const FENTANIL_INDUCAO_RANGE = 3,
    FENTANIL_INDUCAO_UNIT = "mcg",
    FENTANIL_INDUCAO_CONCENTRATION_ML = 8,
    MIDAZOLAM_INDUCAO_RANGE = 0.3,
    MIDAZOLAM_INDUCAO_UNIT = "mg",
    MIDAZOLAM_INDUCAO_CONCENTRATION_ML = 0.1,
    SUCCINILCOLINA_INDUCAO_RANGE = 1,
    SUCCINILCOLINA_INDUCAO_UNIT = "mg",
    SUCCINILCOLINA_INDUCAO_CONCENTRATION_ML = 1;

  const FENTANIL_MANUTENCAO_RANGE_MIN = 0.5,
    FENTANIL_MANUTENCAO_RANGE_MAX = 5,
    FENTANIL_MANUTENCAO_UNIT = "mcg/hora",
    FENTANIL_MANUTENCAO_CONCENTRATION_ML = 8,
    MIDAZOLAM_MANUTENCAO_RANGE_MIN = 20,
    MIDAZOLAM_MANUTENCAO_RANGE_MAX = 600,
    MIDAZOLAM_MANUTENCAO_UNIT = "mcg/hora",
    MIDAZOLAM_MANUTENCAO_CONCENTRATION_ML = 100,
    NORADRENALINA_MANUTENCAO_RANGE_MIN = 12,
    NORADRENALINA_MANUTENCAO_RANGE_MAX = 18,
    NORADRENALINA_MANUTENCAO_UNIT = "mcg/hora",
    NORADRENALINA_MANUTENCAO_CONCENTRATION_ML = 32,
    NORADRENALINA_MANUTENCAO_CONCENTRATION_2X_ML = 64,
    NORADRENALINA_MANUTENCAO_CONCENTRATION_4X_ML = 128;

  const changeDoses = (weight) => {
    $("#dose_fentanil_inducao").text(
      `${FENTANIL_INDUCAO_RANGE * weight}${FENTANIL_INDUCAO_UNIT} >> ${
        (FENTANIL_INDUCAO_RANGE * weight) / FENTANIL_INDUCAO_CONCENTRATION_ML
      }ml`
    );
    $("#dose_midazolam_inducao").text(
      `${MIDAZOLAM_INDUCAO_RANGE * weight}${MIDAZOLAM_INDUCAO_UNIT} >> ${
        (MIDAZOLAM_INDUCAO_RANGE * weight) / MIDAZOLAM_INDUCAO_CONCENTRATION_ML
      }ml`
    );
    $("#dose_succinilcolina_inducao").text(
      `${
        SUCCINILCOLINA_INDUCAO_RANGE * weight
      }${SUCCINILCOLINA_INDUCAO_UNIT} >> ${
        (SUCCINILCOLINA_INDUCAO_RANGE * weight) /
        SUCCINILCOLINA_INDUCAO_CONCENTRATION_ML
      }ml`
    );

    $("#dose_fentanil_manutencao").text(
      `${FENTANIL_MANUTENCAO_RANGE_MIN * weight}${FENTANIL_MANUTENCAO_UNIT} - ${
        FENTANIL_MANUTENCAO_RANGE_MAX * weight
      }${FENTANIL_MANUTENCAO_UNIT} >> ${
        (FENTANIL_MANUTENCAO_RANGE_MIN * weight) /
        FENTANIL_MANUTENCAO_CONCENTRATION_ML
      }ml/hora - ${
        (FENTANIL_MANUTENCAO_RANGE_MAX * weight) /
        FENTANIL_MANUTENCAO_CONCENTRATION_ML
      }ml/hora`
    );
    $("#dose_midazolam_manutencao").text(
      `${
        MIDAZOLAM_MANUTENCAO_RANGE_MIN * weight
      }${MIDAZOLAM_MANUTENCAO_UNIT} - ${
        MIDAZOLAM_MANUTENCAO_RANGE_MAX * weight
      }${MIDAZOLAM_MANUTENCAO_UNIT} >> ${
        (MIDAZOLAM_MANUTENCAO_RANGE_MIN * weight) /
        MIDAZOLAM_MANUTENCAO_CONCENTRATION_ML
      }ml/hora - ${
        (MIDAZOLAM_MANUTENCAO_RANGE_MAX * weight) /
        MIDAZOLAM_MANUTENCAO_CONCENTRATION_ML
      }ml/hora`
    );
    $("#dose_noradrenalina_manutencao_padrao").text(
      `${
        NORADRENALINA_MANUTENCAO_RANGE_MIN * weight
      }${NORADRENALINA_MANUTENCAO_UNIT} - ${
        NORADRENALINA_MANUTENCAO_RANGE_MAX * weight
      }${NORADRENALINA_MANUTENCAO_UNIT} >> ${
        (NORADRENALINA_MANUTENCAO_RANGE_MIN * weight) /
        NORADRENALINA_MANUTENCAO_CONCENTRATION_ML
      }ml/hora - ${
        (NORADRENALINA_MANUTENCAO_RANGE_MAX * weight) /
        NORADRENALINA_MANUTENCAO_CONCENTRATION_ML
      }ml/hora`
    );
    $("#dose_noradrenalina_manutencao_concentrada").text(
      `${
        NORADRENALINA_MANUTENCAO_RANGE_MIN * weight
      }${NORADRENALINA_MANUTENCAO_UNIT} - ${
        NORADRENALINA_MANUTENCAO_RANGE_MAX * weight
      }${NORADRENALINA_MANUTENCAO_UNIT} >> ${
        (NORADRENALINA_MANUTENCAO_RANGE_MIN * weight) /
        NORADRENALINA_MANUTENCAO_CONCENTRATION_2X_ML
      }ml/hora - ${
        (NORADRENALINA_MANUTENCAO_RANGE_MAX * weight) /
        NORADRENALINA_MANUTENCAO_CONCENTRATION_2X_ML
      }ml/hora`
    );
    $("#dose_noradrenalina_manutencao_2x_concentrada").text(
      `${
        NORADRENALINA_MANUTENCAO_RANGE_MIN * weight
      }${NORADRENALINA_MANUTENCAO_UNIT} - ${
        NORADRENALINA_MANUTENCAO_RANGE_MAX * weight
      }${NORADRENALINA_MANUTENCAO_UNIT} >> ${
        (NORADRENALINA_MANUTENCAO_RANGE_MIN * weight) /
        NORADRENALINA_MANUTENCAO_CONCENTRATION_4X_ML
      }ml/hora - ${
        (NORADRENALINA_MANUTENCAO_RANGE_MAX * weight) /
        NORADRENALINA_MANUTENCAO_CONCENTRATION_4X_ML
      }ml/hora`
    );
  };

  $("input#weight").keyup((e) => {
    changeDoses(e.target.value);
  });

  $("input#weight").change((e) => {
    changeDoses(e.target.value);
  });
});

/**
 * Doses de infusão
 * TODO Primeiro eu calculo quantas ampolas para o peso do paciente, depois coloco numa ampola de 20ml
 */