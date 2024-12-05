from urllib.parse import urlparse, parse_qs
import pandas as pd


# Define a function to extract components from a URL
def extract_url_components(url):
    try:
        parsed_url = urlparse(url)
        subdomain, domain, tld = '', '', ''

        if parsed_url.hostname:
            parts = parsed_url.hostname.split('.')
            if len(parts) > 2:
                subdomain = '.'.join(parts[:-2])
                domain = parts[-2]
                tld = parts[-1]
            elif len(parts) == 2:
                domain = parts[0]
                tld = parts[1]

        # Extract query parameters as a concatenated string
        query_parameters = parse_qs(parsed_url.query)
        query = '&'.join([f"{key}={','.join(value)}" for key, value in query_parameters.items()])

        return {
            'scheme': parsed_url.scheme,
            'subdomain': subdomain,
            'domain': domain,
            'top_level_domain': tld,
            'port': parsed_url.port,
            'path': parsed_url.path,
            'query': query,
            'fragment': parsed_url.fragment
        }
    except Exception as e:
        # Return empty or default values if parsing fails
        return {
            'scheme': None,
            'subdomain': None,
            'domain': None,
            'top_level_domain': None,
            'port': None,
            'path': None,
            'query': None,
            'fragment': None,
            'error': str(e)  # For debugging purposes
        }


# Load the dataset
file_path = 'Phishing URLs.csv'
data = pd.read_csv(file_path)

# Apply the function to extract components for each URL
url_components = data['url'].apply(extract_url_components)

# Convert the extracted components into a DataFrame
components_df = pd.DataFrame(url_components.tolist())

# Combine with the original data
result_df = pd.concat([data, components_df], axis=1)

# Save or display the resulting DataFrame
result_df.to_csv('Phishing_URLs_with_Components.csv', index=False)

# Load the dataset
file_path = 'URL dataset.csv'
data = pd.read_csv(file_path)

# Apply the function to extract components for each URL
url_components = data['url'].apply(extract_url_components)

# Convert the extracted components into a DataFrame
components_df = pd.DataFrame(url_components.tolist())

# Combine with the original data
result_df = pd.concat([data, components_df], axis=1)

# Save or display the resulting DataFrame
result_df.to_csv('URL_dataset_with_Components.csv', index=False)



