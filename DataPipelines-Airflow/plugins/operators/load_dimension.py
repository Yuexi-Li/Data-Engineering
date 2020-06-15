from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 insert_select_query="",
                 insert_after_delete=True,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.insert_select_query = insert_select_query
        self.insert_after_delete = insert_after_delete
         

    

    def execute(self, context):
        self.log.info(f"Loading data from staging tables to the {self.table}")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if(self.insert_after_delete):
            self.log.info(f"Removi data from dimension table: {self.table}")
            redshift.run("TRUNCATE TABLE {}".format(self.table))
        
        self.log.info(f"Load data to the dimension table: {self.table}")
        insert_query = """
            INSERT INTO {table}
            {insert_select_query}
        """.format(table = self.table,
                   insert_select_query = self.insert_select_query)
        redshift.run(insert_query)
        
        self.log.info(f"Finished loading data from dimension tables to the {self.table}")