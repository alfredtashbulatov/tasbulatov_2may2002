SELECT DISTINCT name FROM  Regions
SELECT (season, edible) FROM  Mushrooms WHERE mushroom_id = (Трубчатые)
SELECT name FROM  Categories order by desc
SELECT (name, description) FROM Mushrooms WHERE category_id = (сьедобные) and primary_region_id = (самые большие по размеру регионы)
SELECT name from Mushrooms where season (весна) and mushroom_id = («Пластинчатые») and size < 6000\