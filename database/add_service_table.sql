-- rank_for_gu 테이블
CREATE TABLE rank_for_gu (
    rank_gu_id INT PRIMARY KEY AUTO_INCREMENT,
    rank_school FLOAT,
    rank_academy FLOAT,
    rank_traffic_accident FLOAT,
    rank_crime FLOAT,
    rank_unhealthy_facility FLOAT,
    rank_park FLOAT,
    rank_library FLOAT,
    rank_hospital FLOAT,
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

CREATE TABLE rank_for_dong(
    rank_dong_id INT PRIMARY KEY AUTO_INCREMENT,
    rank_rent FLOAT,
    rank_hospital FLOAT,
    gu_id INT,
    dong_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id),
    FOREIGN KEY (dong_id) REFERENCES dong(dong_id)
);