import re
import string
import tldextract
from urllib.parse import urlparse

# Keywords that are commonly used in phishing URLs
malicious_keywords = [
    "login", "secure", "account", "update", "verify", "bank", "paypal", "security", "password", "confirm",
    "signin", "signup", "verify", "confirm", "update", "secure", "account", "password", "username",
    "credit", "card", "payment", "billing", "invoice", "receipt", "refund"
]

def extract_features_common(url): # Shared feature extraction logic
    url = url.rstrip('/')
    features = {} # dictionary to hold extracted features
    parsed = urlparse(url) # splits the URL into scheme, path, domain, etc
    ext = tldextract.extract(url) # splits the URL into domain, subdomain and suffix only

    # Basic URL features
    features['url_length'] = len(url)
    features['domain_length'] = len(ext.domain)
    features['path_length'] = len(parsed.path)
    features['query_length'] = len(parsed.query)
    
    # Domain features
    features['num_subdomains'] = len(ext.subdomain.split('.')) if ext.subdomain else 0
    features['has_https'] = int(parsed.scheme == 'https')
    features['has_www'] = int('www' in url.lower())
    
    # Security features - only the most reliable indicators
    features['malicious_keyword'] = int(any(kw in url.lower() for kw in malicious_keywords))
    features['unusual_domain'] = int(bool(re.search(r'\d', ext.domain)) or bool(re.search(r'[^a-zA-Z0-9\-]', ext.domain)))
    features['has_suspicious_tld'] = int(ext.suffix in ['tk', 'ml', 'ga', 'cf', 'gq', 'xyz', 'top', 'club', 'site', 'online'])
    
    # Character analysis - simplified
    features['number_of_hyphens'] = url.count('-')
    features['number_of_underscores'] = url.count('_')
    features['number_of_dots'] = url.count('.')
    features['number_of_slashes'] = url.count('/')
    features['number_of_equals'] = url.count('=')
    features['number_of_question_marks'] = url.count('?')
    features['number_of_ampersands'] = url.count('&')
    features['number_of_percentages'] = url.count('%')
    
    # Advanced features - only the most important ones
    features['contains_ip'] = int(bool(re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', url)))
    features['has_at_symbol'] = int('@' in url)
    features['num_digits'] = sum(c.isdigit() for c in url)
    features['num_letters'] = sum(c.isalpha() for c in url)
    
    # Special character analysis - more conservative
    common_url_chars = set(':/.-')
    features['num_special_chars'] = sum(c in string.punctuation and c not in common_url_chars for c in url)
    
    # URL structure features
    features['has_query_params'] = int(len(parsed.query) > 0)
    features['has_fragment'] = int(len(parsed.fragment) > 0)
    features['path_depth'] = len([x for x in parsed.path.split('/') if x]) if parsed.path else 0
    
    # Domain age indicators (suspicious TLDs)
    features['has_short_tld'] = int(len(ext.suffix) <= 2)
    features['has_long_tld'] = int(len(ext.suffix) >= 4)
    
    return features

# Feature names list
feature_names = [
    "url_length", "domain_length", "path_length", "query_length",
    "num_subdomains", "has_https", "has_www",
    "malicious_keyword", "unusual_domain", "has_suspicious_tld",
    "number_of_hyphens", "number_of_underscores", "number_of_dots", 
    "number_of_slashes", "number_of_equals", "number_of_question_marks",
    "number_of_ampersands", "number_of_percentages",
    "contains_ip", "has_at_symbol", "num_digits", "num_letters",
    "num_special_chars", "has_query_params", "has_fragment", "path_depth",
    "has_short_tld", "has_long_tld"
] 