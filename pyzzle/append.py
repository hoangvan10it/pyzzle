from pyzzle import DataLoader


class DataLoaderAppend(DataLoader):

    def __init__(self, config, spark=None, params={}):
        super(DataLoaderAppend, self).__init__(
            config, spark=spark, params=params)

        # Both 'insert' and 'append' operation are allowed
        assert self.config["target"]["operation"] in [
            "insert", "append"]

    def step_06_operate(self, generate_sql=False):
        if "table" in self.config["target"]:
            target_table = self.config["target"]["table"]
        elif "path" in self.config["target"]:
            target_table = "delta.`{}`".format(target_table)

        script = f"""INSERT INTO {target_table} SELECT * FROM __source_view"""
        if generate_sql:
            return script
        else:
            return self.execute_script(script)
