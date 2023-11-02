# Example user access logs
user_access_logs = [
    "John accessed Page1",
    "Ema accessed Page2",
    "John accessed Page2",
    "Steve accessed Page1",
    "Ema accessed Page3",
    "Steve accessed Page2",
    "John accessed Page3",
    "Ema accessed Page1",
    "Steve accessed Page3",
]

# Analyzing user access patterns
user_page_counts = {}
for log in user_access_logs:
    user, page = log.split(" accessed ")
    if user in user_page_counts:
        user_page_counts[user].append(page)
    else:
        user_page_counts[user] = [page]

# Print the user access patterns
print("User Access Patterns:")
for user, pages in user_page_counts.items():
    print(f"User {user} accessed pages: {', '.join(pages)}")
