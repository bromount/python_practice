#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:38:19 2018

@author: bromount
"""

"""
This script uses the Vision API's text detection capabilities to find a text
based on an image's content.

To run the example, install the necessary libraries by running:

    pip install -r requirements.txt

Run the script on an image to get text, E.g.:

    ./text_detection.py <path-to-image>
"""

import argparse
import os

from utils import Service, encode_image


def main(photo_file):
    """Run a text detection request on a single image"""
    print "Into Main Function"
    access_token = os.environ.get('VISION_API')
    print access_token
    service = Service('vision', 'v1', access_token=access_token)

    with open(photo_file, 'rb') as image:
        print "into with section"
        base64_image = encode_image(image)
        body = {
            'requests': [{
                'image': {
                    'content': base64_image,
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 1,
                }]

            }]
        }
        print "out"
        response = service.execute(body=body)
        print "After response"
        text = response['responses'][0]['textAnnotations'][0]['description']
        print "after text"
        print('Found text: {}'.format(text))

if __name__ == '__main__':
    print "Main"
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to detect text.')
    args = parser.parse_args()
    main(args.image_file)
