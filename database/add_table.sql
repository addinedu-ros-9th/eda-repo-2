CREATE TABLE traffic_accident (
    accident_id INT PRIMARY KEY AUTO_INCREMENT,
    accident_count INT,      
    gu_id INT,                        
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);
