function getMonthName(monthNumber) {
  const date = new Date();
  date.setMonth(monthNumber - 1);

  // 👇️ using the visitor's default locale
  return date.toLocaleString([], {
    month: 'long',
  });
}