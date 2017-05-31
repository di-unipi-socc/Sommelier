import unittest
import topologyvalidator

class Test_Sommelier(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_0(self):

        path = "tests/tosca_elk.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        isCorrect = True
        for nodeName in validation:
            reqs = validation.get(nodeName).keys()
            for req in reqs:
                infoList = validation.get(nodeName).get(req)
                for info in infoList:
                    isCorrect = False
        self.assertEqual(isCorrect, True)

    def test_1_1(self):

        path = "tests/tosca_elk_1-1.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('kibana', validation)
        self.assertIn('hosted_on', validation['kibana'])
        self.assertEqual(1.1, validation['kibana']['hosted_on'][0][0])

    def test_1_1_missingTarget(self):

        path = "tests/tosca_elk_mod.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('app_rsyslog', validation)
        self.assertIn('log_endpoint', validation['app_rsyslog'])
        self.assertEqual(1.1, validation['app_rsyslog']['log_endpoint'][0][0])

    def test_1_2(self):

        path = "tests/tosca_elk_1-2.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('mongo_db', validation)
        self.assertIn('host', validation['mongo_db'])
        self.assertListEqual(validation['mongo_db']['host'][0], [1.2, 'tosca.nodes.Compute', 'mongo_server'])

    def test_1_3(self):

        path = "tests/tosca_elk_1-3.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('logstash', validation)
        self.assertIn('search_endpoint', validation['logstash'])
        self.assertEqual(1.3, validation['logstash']['search_endpoint'][0][0])

    def test_1_4(self):

        path = "tests/tosca_elk_1-4.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('kibana', validation)
        self.assertIn('search_endpoint', validation['kibana'])
        self.assertListEqual(validation['kibana']['search_endpoint'][0], [1.4, 'elasticsearch', 'tosca.capabilities.Endpoint'])        

        self.assertIn('logstash', validation)
        self.assertIn('search_endpoint', validation['logstash'])
        self.assertListEqual(validation['logstash']['search_endpoint'][0], [1.4, 'elasticsearch', 'tosca.capabilities.Endpoint'])        

    def test_1_5(self):

        path = "tests/tosca_elk_1-5.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('logstash', validation)
        self.assertIn('search_endpoint', validation['logstash'])
        self.assertEqual(1.5, validation['logstash']['search_endpoint'][0][0])            

    def test_2_1(self):

        path = "tests/tosca_elk_2-1.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('logstash', validation)
        self.assertIn('search_endpoint', validation['logstash'])
        self.assertListEqual(validation['logstash']['search_endpoint'][0], [2.1, 'search_endpoint'])        

    def test_2_2(self):

        path = "tests/tosca_elk_2-2.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('logstash', validation)
        self.assertIn('search_endpoint', validation['logstash'])
        self.assertListEqual(validation['logstash']['search_endpoint'][0], [2.2, 'elasticsearch'])  

    def test_3_1(self):

        path = "tests/tosca_elk_3-1.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('logstash', validation)
        self.assertIn('search_endpoint', validation['logstash'])
        self.assertListEqual(validation['logstash']['search_endpoint'][0], [3.1, 'tosca.nodes.SoftwareComponent.Logstash']) 

    def test_3_2(self):

        path = "tests/tosca_elk_3-2.yaml"
        v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        self.assertIn('logstash', validation)
        self.assertIn('search_endpoint', validation['logstash'])
        self.assertListEqual(validation['logstash']['search_endpoint'][0], [3.2, 'tosca.nodes.SoftwareComponent.Logstash', 'elasticsearch']) 
