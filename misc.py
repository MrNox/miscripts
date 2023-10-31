def dec2hex(x):
    """
    Se toma de nibble a nibble (4-bit) y se convierte a string,
    si es menor a 9 entonces le sumamos 0x30, para obtener el número en ascii.

    Si es mayor a 9 entonces le sumamos 0x37, para obtener la letra en ascii.
    Esto es así porque 'A' sería el "cero" y tendríamos que
    sumarle un valor para convertirlo a ascii, 0xA == 10, entonces 'A' == 0x41 == 65,
    le restamos el - 10 == 0x37 == 55
    """

    s = ''
    while (x > 0):
        y = (x & 0xf)

        # y += (ord('A')-10) if (y > 9) else ord('0')
        # is same:
        y += 0x37 if (y > 9) else 0x30

        s = chr(y) + s
        x >>= 4


def align(n, a):
    """
    Alinea un número 'n' a un múltiplo de a.
    """
    return (n + (a - 1)) & -a


def padding(n, a):
    """
    Calcula el padding necesario para alinear un número 'n' a un múltiplo de a.
    """
    return -n & (a - 1)
    # same:
    # return align(n, a) - n


def ror32(x, n):
    """
    ror fixed to 32-bit.
    """
    return ((x >> n) | (x << (32 - n))) & 0xffffffff


def rol32(x, n):
    """
    rol fixed to 32-bit.
    """
    return ((x << n) | (x >> (32 - n))) & 0xffffffff


def ror64(x, n):
    """
    ror fixed to 64-bit.
    """
    return ((x >> n) | (x << (64 - n))) & (1 << 64) - 1


def rol64(x, n):
    """
    rol fixed to 64-bit.
    """
    return ((x << n) | (x >> (64 - n))) & (1 << 64) -1


def bswap32(x):
    """
    bswap fixed to 32-bit.
    """
    return rol32(x, 8) & 0x00ff00ff | ror32(x, 8) & 0xff00ff00


def bswap64(x):
    """
    bswap fixed to 64-bit.
    """

    high = x >> 32
    low = x & (1 << 32) - 1
    return (bswap32(low) << 32) | bswap32(high)

s = dec2hex(64000000)
print(s)

