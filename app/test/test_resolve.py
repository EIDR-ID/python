from app.manager import SessionManager
import unittest

from app.scheme.com.movielabs.schema.md.v2.pkg_8.md import StringCompilationCompilationClass
from app.scheme.org.doi.pkg_2010.doischema_avs import CreationStructuralType
from app.services.metadata import FullMeta


class TestResolve(unittest.TestCase):

    def test_resolve(self):
        ses = SessionManager.from_default()
        out: FullMeta = ses.resolve("10.5240/E482-BB71-F7DD-8584-FEB1-F")

        self.assertEqual(out.base_meta.structural_type, CreationStructuralType.ABSTRACTION)
        self.assertEqual(out.extra_meta.compilation_info["compilation_class"]["value"], StringCompilationCompilationClass.SERIES)

        # Test different structural types
        self.assertNotEqual(ses.resolve("10.5240/FD02-E0FC-B5BD-A7EA-77E2-U").extra_meta.edit_info, None) # edit
        self.assertNotEqual(ses.resolve("10.5240/90B8-5465-14DD-8FBC-8843-A").extra_meta.series_info, None) # series
        self.assertNotEqual(ses.resolve("10.5240/B3C3-5B2E-B3C4-E3AB-20DF-L").extra_meta.episode_info, None) # episode
        self.assertNotEqual(ses.resolve("10.5240/B514-FB14-DF6D-B857-BAAF-4").extra_meta.composite_info, None) # composite
        self.assertNotEqual(ses.resolve("10.5240/BBA5-429A-BA1A-1BFE-5317-D").extra_meta.season_info, None) # season
        self.assertNotEqual(ses.resolve("10.5240/F183-7C2F-AABC-64A9-D4BE-Y").extra_meta.alternate_content_info, None) # alternate content
        self.assertNotEqual(ses.resolve("10.5240/DB80-AEE8-1CF5-03F3-7293-9").extra_meta.supplemental_content_info, None) # supplemental content
        self.assertNotEqual(ses.resolve("10.5240/CEFD-A579-C781-CC22-73F6-1").extra_meta.promotion_info, None) # promotion
        self.assertNotEqual(ses.resolve("10.5240/4CFA-B9A4-6F23-6AF1-FAF3-2").extra_meta.packaging_info, None) # packaging
        print()

    def test_service_resolve(self):
        ses = SessionManager.from_default()
        res = ses.service_resolve("10.5239/3472-D276")
        print(res)
        self.assertEqual(res.service_name["display_name"], "Apple TV+")

    def test_party_resolve(self):
        ses = SessionManager.from_default()
        res = ses.party_resolve("10.5237/03F3-6600")
        self.assertEqual(res.party_name["display_name"], "11TH Hour Production and Entertainment Company")
