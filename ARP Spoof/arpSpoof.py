import argparse
import time
import sys
from typing import Tuple
from scapy.all import ARP, Ether, srp, sendp


def get_arguments() -> Tuple[str, str]:
    """Parses command-line arguments and returns target and gateway IP addresses."""
    parser = argparse.ArgumentParser()