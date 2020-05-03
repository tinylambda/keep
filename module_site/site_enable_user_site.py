import site


status = {
    None: 'Disable for security',
    True: 'Enabled',
    False: 'Disable by command-line option',
}

print('Flag: ', site.ENABLE_USER_SITE)
print('Meaning: ', status[site.ENABLE_USER_SITE])

