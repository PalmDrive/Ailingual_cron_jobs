from __future__ import absolute_import
from crontab import CronTab


"""
Task Scheduler
==========
This module manages periodic tasks using cron.
"""


class CronManager:

    def __init__(self):
        self.cron = CronTab(user=True)

    def remove_all(self):
        self.cron.remove_all()
        self.cron.write()
        print self.cron.render()

    def add_minutely(self, name, user, command, environment=None):
        """
        Add an hourly cron task
        """
        cron_job = self.cron.new(command=command, user=user)
        cron_job.minute.every(2)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print self.cron.render()
            return True

    def add_hourly(self, name, user, command, environment=None):
        """
        Add an hourly cron task
        """
        cron_job = self.cron.new(command=command, user=user)
        cron_job.minute.on(0)
        cron_job.hour.during(0, 23)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print self.cron.render()
            return True

    def add_daily(self, name, user, command, environment=None):
        """
        Add a daily cron task
        """
        cron_job = self.cron.new(command=command, user=user)
        cron_job.minute.on(0)
        cron_job.hour.on(0)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print self.cron.render()
            return True

    def add_weekly(self, name, user, command, environment=None):
        """
        Add a weekly cron task
        """
        cron_job = self.cron.new(command=command)
        cron_job.minute.on(0)
        cron_job.hour.on(0)
        cron_job.dow.on(1)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print self.cron.render()
            return True

    def add_monthly(self, name, user, command, environment=None):
        """
        Add a monthly cron task
        """
        cron_job = self.cron.new(command=command)
        cron_job.minute.on(0)
        cron_job.hour.on(0)
        cron_job.day.on(1)
        cron_job.month.during(1, 12)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print self.cron.render()
            return True

    def add_quarterly(self, name, user, command, environment=None):
        """
        Add a quarterly cron task
        """
        cron_job = self.cron.new(command=command)
        cron_job.minute.on(0)
        cron_job.hour.on(0)
        cron_job.day.on(1)
        cron_job.month.on(3, 6, 9, 12)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print self.cron.render()
            return True

    def add_anually(self, name, user, command, environment=None):
        """
        Add a yearly cron task
        """
        cron_job = self.cron.new(command=command)
        cron_job.minute.on(0)
        cron_job.hour.on(0)
        cron_job.month.on(12)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print self.cron.render()
            return True
