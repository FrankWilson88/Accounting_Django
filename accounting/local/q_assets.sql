USE accounting;

CREATE VIEW IF NOT EXISTS vAccountsRecievable AS 
SELECT
  accountsReceivable.timestamp AS timestamp,
  accountsReceivable.snid AS snid,
  accountsReceivable.description AS description,
  SUM(valueLoaned) AS debit,
  SUM(valuePayed) - SUM(defaultAmount) AS credit,
  SUM(defaultAmount) AS totalDefault,
  SUM(valueLoaned) - SUM(valuePayed) AS difference,
  SUM(unitsLoaned) AS unitsLoaned
  accountsReceivable.dateOpened AS dateOpened,
  accountsReceivable.dateClosed AS dateClosed,
  accountsReceivable.dueDate AS dueDate,
  accountsReceivable.customerID AS customerID,
  accountsReceivable.recieptID AS recieptID
FROM accountsReceivable
GROUP BY accountsReceivable.snid
;

CREATE VIEW IF NOT EXISTS vInventory AS 
SELECT
  vRawMaterials.debit + vStoreInventory.qsi1.debit AS debit,
  vRawMaterials.credit + vStoreInventory.credit AS credit,
  (vRawMaterials.debit + vStoreInventory.qsi1.debit) - (vRawMaterials.credit + vStoreInventory.credit) AS dif
FROM vRawMaterials, vStoreInventory
;

CREATE VIEW IF NOT EXISTS qb1 AS
SELECT
  SUM(debit) AS debit,
  SUM(credit) AS credit,
  SUM(debit) - SUM(credit) AS dif,
  SUM(debit) / SUM(depreciationLife) AS depreciationCost
FROM building
;
