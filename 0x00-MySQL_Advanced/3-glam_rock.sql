-- Active: 1691578679906@@127.0.0.1@5432@hbtn_0d_tvshows

-- list all bands with Glam rock as their main style, sorted by the number

-- of fans they have (in descending order)

SELECT
    band_name,
    IFNULL(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
