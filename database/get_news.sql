select Contents as Новость, DateTime as 'Время добавления', Name as Сайт  from News
join WebSites
where News.WebSiteId=WebSites.Id