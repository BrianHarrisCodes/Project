
-----------------------------------------------------------------------
-- Populate Property Address Data


SELECT *
FROM NashHousing
ORDER BY ParcelID


SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress,b.PropertyAddress)
FROM NashHousing a
JOIN NashHousing b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress IS NULL

UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress,b.PropertyAddress)
FROM NashHousing a
JOIN NashHousing b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress is NULL

SELECT PropertyAddress
FROM NashHousing
WHERE PropertyAddress is NULL


-------------------------------------------------------------------------
-- Breaking out Full Address into individual Columns (Address, City, State)

--Property Address

SELECT PropertyAddress
FROM NashHousing


ALTER TABLE NashHousing
ADD PropertyAddressStreet NVARCHAR(255);

UPDATE NashHousing
SET PropertyAddressStreet = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1) 


ALTER TABLE NashHousing
ADD PropertyAddressCity NVARCHAR(255);

UPDATE NashHousing
SET PropertyAddressCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1 , LEN(PropertyAddress)) 

SELECT PropertyAddressStreet, PropertyAddressCity
FROM NashHousing


-- Owner Address

SELECT OwnerAddress
FROM NashHousing


ALTER TABLE NashHousing
ADD OwnerAddressStreet NVARCHAR(255);

UPDATE NashHousing
SET OwnerAddressStreet = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)


ALTER TABLE NashHousing
ADD OwnerAddressCity NVARCHAR(255);

UPDATE NashHousing
SET OwnerAddressCity = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)


ALTER TABLE NashHousing
ADD OwnerAddressState NVARCHAR(255);

UPDATE NashHousing
SET OwnerAddressState = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)


------------------------------------------------------------------------------
-- Change "Y" to "Yes" and "N" to "No" in the "Sold as Vacant" field

SELECT DISTINCT SoldAsVacant
FROM NashHousing


UPDATE NashHousing
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	WHEN SoldAsVacant = 'N' THEN 'No'
	ELSE SoldAsVacant
	END


	
-------------------------------------------------------------------------------
-- Remove Duplicates

WITH RowNumCTE AS(
SELECT *,
   ROW_NUMBER() OVER (
   PARTITION BY ParcelID,
                PropertyAddress,
				SalePrice,
				SaleDate,
				LegalReference
				ORDER BY
				   UniqueID
				   ) row_num

FROM NashHousing
)
--SELECT *
DELETE
FROM RowNUMCTE
WHERE row_num > 1
--ORDER BY PropertyAddress



----------------------------------------------------------------
-- Delete Unused Columns


SELECT *
FROM NashHousing

ALTER TABLE NashHousing
DROP COLUMN SaleDate, OwnerAddress, TaxDistrict, PropertyAddress