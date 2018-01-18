````
COPY (SELECT * FROM clinical_data) TO '/tmp/clinical_data.csv' (format csv, delimiter ';');
```