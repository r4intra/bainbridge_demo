import requests
import simplejson as json
from typing import Dict


class RxNormIngredientATCConceptCall(object):
    """
    Class encapsulates the data needed to call the RxNorm API and return the linked data elements for ATC mapping
    from a string.
    """

    def __init__(self, ingredient_name: str):
        self.ingredient_name = ingredient_name
        self.rxnorm_api_base = 'https://rxnav.nlm.nih.gov/REST/'
        self.get_rxnorm_code_url = '{base}approximateTerm.json?term={ingredient_name}&maxEntries=1'.format(
            ingredient_name=self.ingredient_name,
            base=self.rxnorm_api_base)  # Limit to top result
        self.rxcui = self.parse_get_rxnorm()
        self.get_atc_code_url = '{base}rxcui/{rxcui}/property?propName=ATC'.format(
            rxcui=self.rxcui,
            base=self.rxnorm_api_base)
        self.atc_code = self.parse_atc_code()

    @staticmethod
    def rx_norm_api_call(url: str) -> Dict:
        results = requests.get(url, headers={'Accept': 'application/json'})
        if results.status_code == 200:
            return json.loads(results.text)

    def parse_get_rxnorm(self) -> str:
        results = RxNormIngredientATCConceptCall.rx_norm_api_call(self.get_rxnorm_code_url)
        if results['approximateGroup'].get('candidate', None) is not None:
            return list(
                set([r.get('rxcui', None) for r in results['approximateGroup']['candidate'] if
                     r['rank'] == '1']))[0]

    def parse_atc_code(self) -> str:
        results = RxNormIngredientATCConceptCall.rx_norm_api_call(self.get_atc_code_url)
        if results['propConceptGroup'] is not None:
            return list(set([r['propValue'] for r in results['propConceptGroup'].get('propConcept', [None])]))[0]


if __name__ == '__main__':
    res = RxNormIngredientATCConceptCall('gabapentin')
    print(res.get_rxnorm_code_url)
    print(res.rxcui)
    print(res.atc_code)
