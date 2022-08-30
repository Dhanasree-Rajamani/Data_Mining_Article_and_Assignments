function calculateDaysBetweenDates(begin, end) {
    var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
    var firstDate = new Date(begin);
    var secondDate = new Date(end);
    var diffDays = Math.round(Math.abs((firstDate.getTime() - secondDate.getTime())/(oneDay)));
    return diffDays;
}

startDate = 01/01/2016;
endDate = 01/01/2017;
numberOfDays = calculateDaysBetweenDates(startDate, endDate);