function verifyIfDateIsRangeCurrentDate() {
  let initialDate = new Date();
  let endDate = new Date();

  initialDate.setDate(initialDate.getDate() - 2);

  endDate.setHours(23, 0, 0);
  initialDate.setHours(0, 0, 0);

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
