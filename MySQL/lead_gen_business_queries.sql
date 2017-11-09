1.
SELECT EXTRACT(month FROM charged_datetime) AS 'Month', SUM(amount) AS 'Billing total'
FROM billing
WHERE EXTRACT(MONTH FROM charged_datetime) = 3 AND EXTRACT(YEAR FROM charged_datetime) = 2012
GROUP BY EXTRACT(month FROM charged_datetime)

2.
SELECT clients.client_id, SUM(billing.amount)
FROM clients
LEFT JOIN billing
ON billing.client_id = clients.client_id
WHERE clients.client_id = 2

3.
SELECT sites.domain_name AS 'Website', clients.client_id AS 'Client ID'
FROM clients
LEFT JOIN sites
ON sites.client_id = clients.client_id
WHERE clients.client_id = 10

4.
SELECT clients.client_id , COUNT(sites.site_id) AS '# Created', MONTHNAME(sites.created_datetime) AS 'MONTH', EXTRACT(YEAR FROM sites.created_datetime) AS 'YEAR'
FROM sites
LEFT JOIN clients
ON sites.client_id = clients.client_id
WHERE clients.client_id = 1
GROUP BY MONTHNAME(sites.created_datetime), EXTRACT(YEAR FROM sites.created_datetime)
ORDER BY EXTRACT(YEAR FROM sites.created_datetime), MONTHNAME(sites.created_datetime)

5.
SELECT sites.domain_name AS website, COUNT(leads.leads_id), DATE_FORMAT(leads.registered_datetime, '%M %e, %Y') as date_created
FROM leads
LEFT JOIN sites
ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01 00:00:01' AND '2011-02-15 23:59:59'
GROUP BY sites.domain_name, DATE_FORMAT(leads.registered_datetime, '%M %e, %Y')

6.
SELECT concat(clients.first_name, ' ', clients.last_name) as client_name, COUNT(leads_id) as number_of_leads
FROM leads
JOIN sites
ON leads.site_id = sites.site_id
JOIN clients
ON clients.client_id = sites.client_id
WHERE leads.registered_datetime BETWEEN '2011-01-01 00:00:01' AND '2011-12-31 23:59:59'
GROUP BY client_name
ORDER BY number_of_leads DESC

7.
SELECT concat(clients.first_name, ' ', clients.last_name) as client_name, COUNT(leads_id) as number_of_leads, MONTH(registered_datetime) AS month_generated
FROM leads
JOIN sites
ON leads.site_id = sites.site_id
JOIN clients
ON clients.client_id = sites.client_id
WHERE YEAR(leads.registered_datetime) = 2011 AND MONTH(leads.registered_datetime) BETWEEN 1 AND 6
GROUP BY client_name, month_generated
ORDER BY month_generated ASC

8.
SELECT
    CONCAT(clients.first_name,
            ' ',
            clients.last_name) AS client_name,
    sites.domain_name AS website,
    COUNT(leads_id) AS number_of_leads,
    DATE_FORMAT(leads.registered_datetime, '%M %e, %Y') AS date
FROM
    leads
        JOIN
    sites ON leads.site_id = sites.site_id
        JOIN
    clients ON clients.client_id = sites.client_id
WHERE
    leads.registered_datetime BETWEEN '2011-01-01 00:00:01' AND '2011-12-31 23:59:59'
GROUP BY website
ORDER BY client_name , number_of_leads DESC

8b.
SELECT
    CONCAT(clients.first_name,
            ' ',
            clients.last_name) AS client_name,
    sites.domain_name AS website,
    COUNT(leads_id) AS number_of_leads
FROM
    leads
        JOIN
    sites ON leads.site_id = sites.site_id
        JOIN
    clients ON clients.client_id = sites.client_id
GROUP BY website
ORDER BY number_of_leads DESC

9.
SELECT
    CONCAT(clients.first_name,
            ' ',
            clients.last_name) AS client_name,
    SUM(billing.amount) AS Total_revenue,
    MONTH(billing.charged_datetime) AS month_charge,
    YEAR(billing.charged_datetime) AS year_charge
FROM
    clients
        JOIN
    billing ON clients.client_id = billing.client_id
GROUP BY year_charge , month_charge
ORDER BY client_name , Total_revenue

10.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) as client_name,
	GROUP_CONCAT(sites.domain_name) as websites
FROM clients
JOIN sites
ON sites.client_id = clients.client_id
GROUP BY client_name
