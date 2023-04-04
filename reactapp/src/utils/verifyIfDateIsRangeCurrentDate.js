function verifyIfDateIsRangeCurrentDate() {
  let initialDate = new Date();
  let endDate = new Date();

  if (initialDate.getHours() > 7) {
    endDate.setDate(initialDate.getDate() + 1);
  } else {
    initialDate.setDate(initialDate.getDate() - 1);
  }

  endDate.setHours(7, 0, 0);
  initialDate.setHours(7, 0, 0);
  return {
    initialDate,
    endDate,
    verifyDate: function (date) {
      const dateTime = date.getTime();

      if (
        this.initialDate.getTime() <= dateTime &&
        this.endDate.getTime() >= dateTime
      ) {
        return true;
      }
      throw new Error("Data está fora do range de datas");
    },
  };
}

export default verifyIfDateIsRangeCurrentDate;
