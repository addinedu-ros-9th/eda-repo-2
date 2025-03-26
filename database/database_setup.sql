-- dong 테이블
CREATE TABLE dong (
    dong_id INT PRIMARY KEY AUTO_INCREMENT,
    dong_name VARCHAR(16),
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

-- crime 테이블
CREATE TABLE crime (
    crime_id INT PRIMARY KEY AUTO_INCREMENT,
    crime_type VARCHAR(16),
    crime_count FLOAT,
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

-- unhealthy_facility 테이블
CREATE TABLE unhealthy_facility (
    unhealty_id INT PRIMARY KEY AUTO_INCREMENT,
    unhealty_type VARCHAR(16),
    unhealty_count FLOAT,
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

-- school 테이블
CREATE TABLE school (
    school_id INT PRIMARY KEY AUTO_INCREMENT,
    school_type VARCHAR(16),
    school_count FLOAT,
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

-- academy 테이블
CREATE TABLE academy (
    academy_id INT PRIMARY KEY AUTO_INCREMENT,
    academy_type VARCHAR(16),
    academy_count FLOAT,
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

-- university 테이블
CREATE TABLE university (
    uni_id INT PRIMARY KEY AUTO_INCREMENT,
    high_graduation FLOAT,
    uni_enrollment FLOAT,
    advancement_rate FLOAT,
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

-- learning_space 테이블
CREATE TABLE learning_space (
    space_id INT PRIMARY KEY AUTO_INCREMENT,
    space_type VARCHAR(16),
    space_count FLOAT,
    gu_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id)
);

-- real_estate 테이블
CREATE TABLE real_estate (
    estate_id INT PRIMARY KEY AUTO_INCREMENT,
    estate_type VARCHAR(16),
    estate_size FLOAT,
    estate_rent FLOAT,
    estate_deposit FLOAT,
    gu_id INT,
    dong_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id),
    FOREIGN KEY (dong_id) REFERENCES dong(dong_id)
);

-- hospital 테이블
CREATE TABLE hospital (
    hospital_id INT PRIMARY KEY AUTO_INCREMENT,
    hospital_type VARCHAR(16),
    hospital_name VARCHAR(16),
    hospital_address VARCHAR(16),
    gu_id INT,
    doro_id INT,
    dong_id INT,
    FOREIGN KEY (gu_id) REFERENCES gu(gu_id),
    FOREIGN KEY (dong_id) REFERENCES dong(dong_id),
    FOREIGN KEY (doro_id) REFERENCES doro(doro_id)
);