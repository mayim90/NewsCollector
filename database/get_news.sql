select Contents as 'Новость', 
       Name as 'Новостной сайт',
	   PostDate as 'Дата публикации'
from News join WebSites
on News.WebSiteId=WebSites.Id