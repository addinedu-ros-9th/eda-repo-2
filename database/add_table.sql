-- CREATE TABLE traffic_accident (
--     accident_id INT PRIMARY KEY AUTO_INCREMENT,
--     accident_count INT,      
--     gu_id INT,                        
--     FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
-- );

CREATE TABLE park(
    park_id INT PRIMARY KEY AUTO_INCREMENT,
    park_type VARCHAR(32),
    park_size DECIMAL(10,2),
    park_for_one DECIMAL(10,2),
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

