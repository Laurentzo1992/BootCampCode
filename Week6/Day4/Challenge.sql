
CREATE or REPLACE FUNCTION age_actor(fn varchar(50), lan varchar(100)) 
RETURNS date AS $birthdate$
BEGIN
   RETURN(SELECT age FROM actors WHERE actors.first_name = fn AND actors.last_name=lan);
END;
$birthdate$ LANGUAGE plpgsql;