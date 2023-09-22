DROP TABLE IF EXISTS claimfile

CREATE TABLE IF NOT EXISTS claimfile(
    id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(id)
    claimfile VARCHAR(20)
)

INSERT INTO claimfile (id, claimfile) values ('1', 'Hello World from PGSQL')
INSERT INTO claimfile (id, claimfile) values ('2', 'Hello Earthlins from PGSQL')
